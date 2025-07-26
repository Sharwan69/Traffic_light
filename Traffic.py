import time
import random
from transitions import Machine

class SmartTrafficLightController:
    # Define FSM states
    states = ['Red', 'Green', 'Yellow', 'Pedestrian']

    def __init__(self):
        # Traffic and pedestrian flags
        self.traffic_waiting = False
        self.pedestrian_request = False
        self.emergency_vehicle = False
        # Simulate queue length (for adaptive green time)
        self.queue_length = 0

        # Create the state machine
        self.machine = Machine(
            model=self,
            states=SmartTrafficLightController.states,
            initial='Red',
            ignore_invalid_triggers=True
        )

        # Add transitions with conditions and triggers
        self.machine.add_transition(
            trigger='detect_traffic', source='Red', dest='Green',
            conditions='is_queue_present'
        )
        self.machine.add_transition(
            trigger='timer_expire', source='Green', dest='Yellow',
            after='start_yellow_phase'
        )
        self.machine.add_transition(
            trigger='timer_expire', source='Yellow', dest='Red'
        )
        self.machine.add_transition(
            trigger='pedestrian_press', source='Green', dest='Pedestrian',
            conditions='is_pedestrian_present', after='start_pedestrian_phase'
        )
        self.machine.add_transition(
            trigger='timer_expire', source='Pedestrian', dest='Red'
        )
        self.machine.add_transition(
            trigger='emergency_override', source='*', dest='Green'
        )

    def is_queue_present(self):
        return self.queue_length > 0

    def is_pedestrian_present(self):
        return self.pedestrian_request

    def start_yellow_phase(self):
        print("Yellow light... (3 seconds)")
        time.sleep(3)  # Simulate yellow duration

    def start_pedestrian_phase(self):
        print("Pedestrian crossing... (5 seconds)")
        time.sleep(5)  # Simulate crossing time

    def adaptive_green_time(self):
        # Green time scales with queue length, capped between 5 and 15 seconds
        return min(15, max(5, self.queue_length * 2))

def simulate_adaptive_traffic_lights(cycles=5):
    ctrl = SmartTrafficLightController()
    for i in range(cycles):
        # Randomly simulate queue length and pedestrian request
        ctrl.queue_length = random.randint(0, 8)
        ctrl.pedestrian_request = bool(random.choice([0, 1]))
        ctrl.emergency_vehicle = bool(random.choices([0, 1], weights=[8, 1])[0])

        print(f"\n--- Cycle {i+1} ---")
        # Priority 1: Emergency vehicle
        if ctrl.emergency_vehicle:
            print("Emergency vehicle detected! Switching to Green immediately.")
            ctrl.emergency_override()
            green_time = ctrl.adaptive_green_time()
            print(f"Green time (emergency): {green_time}s")
            time.sleep(green_time)
            ctrl.timer_expire()
            ctrl.timer_expire()
            continue

        # Regular operation
        if ctrl.state == 'Red' and ctrl.is_queue_present():
            print(f"Detected {ctrl.queue_length} cars waiting.")
            ctrl.detect_traffic()
            green_time = ctrl.adaptive_green_time()
            print(f"Green time: {green_time}s")
            time.sleep(green_time)
            if ctrl.is_pedestrian_present():
                print("Pedestrian button pressed during green.")
                ctrl.pedestrian_press()
                ctrl.timer_expire()
            else:
                ctrl.timer_expire()
                ctrl.timer_expire()
        elif ctrl.state == 'Red':
            print("No vehicles detected. Remaining on Red.")
            time.sleep(2)

# Example test run
if __name__ == "__main__":
    simulate_adaptive_traffic_lights(cycles=5)
