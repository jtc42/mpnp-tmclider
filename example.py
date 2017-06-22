#!/usr/bin/env python

import time
import TMCM

COMS = ['COM3', 'COM5'] # List of COM ports to use

motors = [TMCM.StepRocker(port=COM, debug=True) for COM in COMS] # Create list of motor objects

# Set key global parameters
for motor in motors:
    motor.set_important_parameters(max_speed=1000,
                                    max_accel=1000,
                                    max_current=128,
                                    standbycurrent=8,
                                    microstep_resolution=8)
    
    # Return key parameters for debugging
    motor.get_globals()
    motor.get_parameters()


def test_motors(motor_objects):
    for motor in motor_objects:
        motor.TMCL.rol(0,500)
        time.sleep(3)
        motor.TMCL.mst(0)
        time.sleep(0.1)
        motor.TMCL.ror(0,500)
        time.sleep(3)
        motor.TMCL.mst(0)
        time.sleep(0.1)

test_motors(motors)