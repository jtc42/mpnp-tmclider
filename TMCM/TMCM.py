
import TMCM.TMCL as TMCL


class StepRocker(object):
    def __init__(self, *args, **kwargs):
        self.TMCL = TMCL.Device(*args, **kwargs)
        #self.motors = range(self.TMCL.num_motors)
        self.motors = [0]
        
        # Angle parameters
        self.offset = 0 # Positional offset
        self.spr = 1000 # Steps per revolution
        self.face = 1 # 1 or -1 based on motor orientation


    def get_globals(self):
        ret = {}
        for key, value in TMCL.GLOBAL_PARAMETER.items():
#            print "GGP:", key + value
            bank, par, name, _, _ = key + value
            ret[name] = self.TMCL.ggp(bank, par)
        return ret


    def get_parameters(self):
        retmotor = [{} for _ in self.motors]
        retsingle = {}
        for mn in self.motors:
            for key, value in TMCL.AXIS_PARAMETER.items():
#                print "GAP:", mn, (key,) + value
                par, name, _, _ = (key,) + value
                if par not in TMCL.SINGLE_AXIS_PARAMETERS:
                    retmotor[mn][name] = self.TMCL.gap(mn, par)
                elif mn == 0:
                    retsingle[name] = self.TMCL.gap(mn, par)
        return retmotor, retsingle
    
    
    def get_speed(self, motor=0):
        value = self.TMCL.gap(motor, 3)
        return value


    def set_important_parameters(self,
                                 max_speed=2000, max_accel=2000,
                                 max_current=72, standbycurrent=32,
                                 microstep_resolution=1, store=False):
        for mn in self.motors:
            self.TMCL.sap(mn, 4, max_speed)
            self.TMCL.sap(mn, 5, max_accel)
            self.TMCL.sap(mn, 6, max_current)
            self.TMCL.sap(mn, 7, standbycurrent)
            self.TMCL.sap(mn, 140, microstep_resolution)
            if store:
                self.TMCL.stap(mn, 4)
                self.TMCL.stap(mn, 5)
                self.TMCL.stap(mn, 6)
                self.TMCL.stap(mn, 7)
                self.TMCL.stap(mn, 140)


    def rotate(self, frequency, motor=0, steps=1):
        microstep_resolution = self.TMCL.gap(motor, 140) # Get microstep resolution from device
        vel = abs(frequency) * steps * (2**microstep_resolution) # Calculate velocity
        
        if frequency>0:
            self.TMCL.ror(motor, vel)
        elif frequency<0:
            self.TMCL.rol(motor, vel)
        else:
            self.TMCL.mst(motor)

    def move(self, position, cmdtype='ABS', motor=0, blocking=False):
        self.TMCL.mvp(motor, cmdtype, position)
        if blocking: # If blocking mode is active
            while self.get_speed() != 0: # While speed is not zero
                continue # Stay inside this blocking while-loop
                
    def angle(self, angle, motor=0, blocking=False):
        position = self.face*(angle/360)*self.spr + self.offset
        self.TMCL.mvp(motor, 'ABS', position)
        if blocking: # If blocking mode is active
            while self.get_speed() != 0: # While speed is not zero
                continue # Stay inside this blocking while-loop

    def stop(self, motor=0):
        self.TMCL.mst(motor)


