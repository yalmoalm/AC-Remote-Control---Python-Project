from AbstractClass import AcAbstract
from LinkedList import LinkedList as ll
import time



class ACRemoteControl(AcAbstract):

    def __init__(self):

        self.power = None
        self.temperatura = 16
        self.mode = None
        self.fan = 1
        self.eco = None
        self.time = None
        self.LL = ll()


    
    def Temperatura(self, press):

        if press == '+':
            self.temperatura += 1

        elif press == '-':
            self.temperatura -= 1   
        
        self.temperatura = max(16, min(self.temperatura, 27)) # Range beetwen 16 -27.          

        self.DisplyScreen()

    
    def Mode(self, press):
        
        if press == None:
            
            self.mode =  'Fan'
        
        else:

            self.mode = self.LL.SearchForSpecificNode(press)

        self.DisplyScreen() 



    def Fan(self, press):

        if self.fan == 'AUTO' and press == 'FAN':  
            self.fan = 1

        if press == 'FAN':
            self.fan += 1

        if self.fan == 4:
            self.fan = 'AUTO'

        self.DisplyScreen()           
        
    
    def Time(self):

        named_tuple = time.localtime() # get struct_time
        self.time = time.strftime("%H:%M", named_tuple)
        return self.time
    
    def Eco(self, press):

        if press == 'OFF':
            
            self.eco = 'Disable'
            self.DisplyScreen()

        elif press == 'ON':

            self.eco = 'Enable'   

        else:

            NameError(f'{data} is not define.')

    
    def DisplyScreen(self):

        print("**************************")
        print("       Air Conditioner    ")
        print("**************************")
        print(f"Power: {self.power}")
        print(f"Temperature: {self.temperatura}°C")
        print(f"Mode: {self.mode}")
        print(f"Fan Speed: {self.fan}")
        print(f"Eco Mode: {self.eco}")
        print(f"Time: {self.Time()}")
        print("**************************")

    def Power(self, press):

        if press == 'OFF':

            self.power = press
            self.eco = None
            self.DisplyScreen()

        elif press == 'ON':

            self.power = press   

        else:

            NameError(f'{data} is not define.')

        






def main():

    RemoteControl = ACRemoteControl()
    RemoteControl.Power('ON')
    RemoteControl.Eco('ON')
    RemoteControl.Mode(4)
    RemoteControl.Fan('FAN')
    RemoteControl.Temperatura('+')
    RemoteControl.Temperatura('+')
    RemoteControl.Temperatura('+')
    RemoteControl.Temperatura('+')
    #RemoteControl.Power('OFF')

 








if __name__ == '__main__':
    main()





