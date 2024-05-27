class k:
    def __init__(self):
        self.__foo = 10
    def methodX(self):
        self.__methodY()
        print(self.__foo)
    def __methodY(self):
        self.__foo += 1
    k()