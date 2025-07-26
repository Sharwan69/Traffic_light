# Smart Traffic Light Controller 🚦

An adaptive traffic light control system using Finite State Machine (FSM) principles with Python. This simulation implements intelligent features like emergency vehicle priority, pedestrian crossing, and adaptive green time based on traffic queue length.

## Features ✨

- **Finite State Machine Model**: 
  - States: Red, Green, Yellow, Pedestrian
  - Transitions with conditions and callbacks
  - Emergency vehicle override capability

- **Smart Adaptive Control**:
  - Dynamic green light duration (5-15 seconds) based on traffic density
  - Dedicated pedestrian crossing phase
  - Priority handling for emergency vehicles

- **Realistic Simulation**:
  - Randomized traffic patterns
  - Visual state transition logging
  - Configurable timing parameters

## Installation ⚙️
pip install transitions

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sharwand9/Traffic_light.git
   cd Traffic_light
