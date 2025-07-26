Smart Traffic Light Simulation
This repository contains a Python simulation of a smart adaptive traffic light controller using a Finite State Machine (FSM) implemented with the transitions library.
It adapts green light durations based on vehicle queue length, handles pedestrian crossing requests, and supports emergency vehicle overrides.

Features
Adaptive green light: Duration depends on detected vehicle queue length.

Pedestrian crossing: Supports requests and safe pedestrian light phases.

Emergency override: Instantly changes the light for emergency vehicles.

FSM logic: Easily extended for more traffic states or smart logic.

Prerequisites
Python 3.7 or higher

Install the required packages:

text
pip install transitions
How to Run
Clone the repository

text
git clone https://github.com/Sharwan69/Traffic_light.git
cd Traffic_light
Install dependencies

text
pip install transitions
Run the simulation

text
python Traffic.py
