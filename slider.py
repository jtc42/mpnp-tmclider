import time
import TMCM

# Slider motor settings
# [thick ring, thin ring]
COMS = ['COM3', 'COM5'] # List of COM ports to use
# Default motor calibration
OFFSETS = [0,0] # Positional offsets for each motor
SPR = [102800, 102800] # Steps per revolution
FACES = [1, -1]

## CREATE MOTORS
print("Creating motor objects...")
motors = [TMCM.StepRocker(port=COM, debug=False) for COM in COMS] # Create list of motor objects

          
## LOAD/SAVE

import pickle

def load_prefs():
    global OFFSETS, SPR, FACES
    print("Loading preferences...")
    OFFSETS, SPR, FACES = pickle.load(open("prefs.pickle", "rb"))

def save_prefs():
    global motors
    OFFSETS = [motor.offset for motor in motors]
    SPR = [motor.spr for motor in motors]
    FACES = [motor.face for motor in motors]
    print("Saving preferences...")
    pickle.dump([OFFSETS, SPR, FACES], open("prefs.pickle", "wb"))

try:
    print("Loading preferences...")
    load_prefs()
except (OSError, IOError) as e:
    print("No preferences file found. Creating one...")
    save_prefs()

# Assign motor calibration
print("Assigning angular calibration properties to motors...")         
for i, motor in enumerate(motors):
    motor.offset = OFFSETS[i]
    motor.spr = SPR[i]
    motor.face = FACES[i]

# Set key global parameters
print("Assigning global parameters to motors...")  
"""
DO NOT MODIFY!
CHANGING MAY RISK DAMAGE TO THE SLIDER DUE TO HIGH MAXIMUM VELOCITY,
AND WILL CHANGE POSITION-ANGLE CALIBRATION!
"""
for motor in motors:
    motor.set_important_parameters(max_speed=1000,
                                   max_accel=1000,
                                   max_current=128,
                                   standbycurrent=8,
                                   microstep_resolution=8)
    
    # Return key parameters for debugging
    motor.get_globals()
    motor.get_parameters()

# Startup functions
def test_motors(motor_objects):
    for motor in motor_objects: # For each motor
        for direction in [-1, 1]: # For forwards and reverse directions
            motor.rotate(direction*5) # Rotate at frequency '5', with direction
            time.sleep(1) # Do this for 3 seconds
            motor.stop() # Stop the motor
            time.sleep(0.1) # Wait for 0.1 seconds

def home_motors(motor_objects, blocking=True):
    for motor in motors:
        motor.move(0, cmdtype='ABS')
    while any([motor.get_speed()!=0 for motor in motor_objects]): # While any motors are moving
        continue # Stay in this blocking loop

# Run startup functions
print("Checking motors...")
test_motors(motors)
print("Homing motors...")
home_motors(motors) # Positional home
[m.angle(0, blocking=True) for m in motors]; # Angular home

print("Motors ready for use.")

