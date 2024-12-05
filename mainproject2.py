'''##PART-1
GeneralNeuron
    ├── SensoryNeuron
    │       ├── Photoreceptor
    │       └── Mechanoreceptor
    └── MotorNeuron
            ├── AlphaMotorNeuron
            └── GammaMotorNeuron'''
class GeneralNeuron():
    def __init__(self,firingRate= 0 ):
        self.firingRate = firingRate
        pass

    def activate(self, stimulus):
        '''calculate firing rate based on the stimulus'''
        pass

class SensoryNeuron(GeneralNeuron):
    def __init__(self, firingRate=0, receptorType=None):
        super().__init__(firingRate)
        self.receptorType = receptorType '''Can be either "light" or "pressure"'''

    def senseStimulus(self,stimulus):
        '''process specific stimulus and activates neuron'''
        pass

class motorNeuron(GeneralNeuron):
    def __init__(self, firingRate=0, targetMuscle=None):
        super().__init__(firingRate)
        self.targetMuscle = targetMuscle 
    def controlMuscle(self):
        '''control muscle based on the activation leve'''
        pass

class photoreceptor(GeneralNeuron):
    def __init__(self, firingRate=0):
        super().__init__(firingRate,receptorType = 'light')
    def lightDetection(self,lightIntensity):
        '''specific light detection behavior'''
        pass
    def senseStimulus(self,lightIntensity):
        '''ovveride to handle light specific detection'''
        pass

class mechanoreceptor(GeneralNeuron):
    def __init__(self, firingRate=0):
        super().__init__(firingRate,receptorType = 'pressure')
    def pressureDetection(self,pressureLevel):
        '''specific pressure detection behavior'''
        pass
    def senseStimulus(self,pressureLevel):
        '''ovveride to handle pressure specific detection'''
        pass

class alphaMotorNeuron(GeneralNeuron):
    def __init__(self, firingRate=0):
        super().__init__(firingRate, targetMuscle = 'skeletal muscle')
    def skeletalMuscleControl(self):
        '''specific skeletal muscle control mechanism'''
        pass
    def controlMuscle(self):
        '''ovveride for skeletal muscle specific control'''
        pass

class gammaMotorNeuron(GeneralNeuron):
        def __init__(self, firingRate=0):
        super().__init__(firingRate, targetMuscle = 'muscle spindle')
        def muscleSpindleControl(self):
            '''specific muscle spindle control mechanism'''
            pass
        def controlMuscle(self):
            '''override for muscle spindle specific control'''
            pass


'''PART 2'''
import numpy as np



    







