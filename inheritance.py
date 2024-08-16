class Animal:
    def __init__(self):
        self.eyes=2
    
    def breathe(self):
        print("inhales oxygen, exhales Carbon dioxide")

class Fish(Animal):
    def __init__(self):
        '''super().__init___() is used when we are inherit from parent class'''
        super().__init__()
        
    def breathe(self):
        '''overrides super class method and can do extratasks '''
        super().breathe()
        print("under water")
        
    
    def swim(self):
        print("swims in the ocean")

nemo=Fish()
nemo.swim()
nemo.breathe()
print(f"nemo has {nemo.eyes} eyes")