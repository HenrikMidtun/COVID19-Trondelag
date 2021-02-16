
from controller import TrondelagController, HelsedirController

class COVIDTerminal:
    def __init__(self):
        self.controller = TrondelagController()
        
    def peek(self, rank: int=3):
        for i in range(rank):
            city_data = self.controller.city_data(rank=i)
            print("\t", city_data['navn'])
            print("Smittede: {}".format(city_data['smittet']))
            print("Døde: {}".format(city_data['dode']))
            print("------------------------------")
        print("Sist oppdatert: {}".format(self.controller.last_updated().strftime("%d. %b %Y -- %H:%M:%S")))


'''
    Printing national numbers
'''
class PeekHelsedir:
    def __init__(self):
        self.controller = HelsedirController()

    def peek(self):
        print("Innlagte:")
        print(self.controller.hospitalized())
        print("Respirator:")
        print(self.controller.respirator())

#covid = COVIDTerminal()
#covid.top()

Peek = PeekHelsedir()
Peek.peek()
