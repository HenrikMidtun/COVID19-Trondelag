#controller.py
'''
    Fetches data from models
    Handles data
    Delievers data
'''
from model import COVID


class TrondelagController:
    
    def __init__(self):
        self.model = COVID()

    #returns dictionary for city based on rank or name.
        
    def last_updated(self):
        return self.model.last_updated
    
    def city_data(self, name=None, rank=0):
        if name != None:
            for item in self.model.data:
                if item['navn'] == name:
                    return item
        i = 0
        for item in self.model.data:
            if i == rank:
                return item
            i+=1
    
    def total_infected(self):
        total = 0
        for item in self.model.data:
            total += int(item['smittet'])
        return total
    
            
    def __cities(self):
        cities = []
        for item in self.model.data:
            cities.append(item['navn'])
        return cities
    
    def update_model(self):
        self.model.update()

