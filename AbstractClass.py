from abc import ABC, abstractmethod

class AcAbstract(ABC):  

    def __init__(self):
        print('Creating AC control.')

    @abstractmethod
    def Temperatura(self):
        pass    

    @abstractmethod
    def Mode(self):
        pass

    @abstractmethod
    def Fan(self):
        pass
    
    @abstractmethod
    def Time(self):
        pass

    @abstractmethod
    def Eco(self):
        pass

    @abstractmethod
    def DisplyScreen(self):
        pass

    @abstractmethod
    def Power(self):
        pass
