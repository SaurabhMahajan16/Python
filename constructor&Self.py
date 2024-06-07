class k:
    '''__ is used for private method or object or variable of a class 
    and init is a constructor which intializes when class instance is created
    whereas self is like this. in java
    Self is used to set instance-specific attributes such as private variabe foo here
    '''
    def __init__(self):
        self.__foo = 10
    def methodX(self):
        self.__methodY()
        print(self.__foo)
    def __methodY(self):
        self.__foo += 1
    
obj=k()
obj.methodX()