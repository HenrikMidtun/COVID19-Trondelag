#controller.py
'''
    Fetches data from models
    Handles data
    Delievers data
'''
from model import COVID, HelseDirektoratet_COVID
from logger import CovidLogger

class TrondelagController:
    
    def __init__(self):
        self.model = COVID()
        self.logger = CovidLogger(self.model)

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
        self.logger.update()

class HelsedirController:

    def __init__(self, category = None):
        self.model = HelseDirektoratet_COVID(category)
        self.category = self.model.category

    def last_updated(self):
        return self.model.last_updated
    
    def hospitalized(self):
        in_hospital = self.model.data[-1]['antInnlagte']
        return in_hospital
    
    def respirator(self):
        on_respirator = 0
        if self.category == "nasjonalt":
            on_respirator = self.model.data[-1]['antRespirator']
        return on_respirator

    def update_model(self):
        self.model.update()
    
    def _print_data(self):
        print(self.model.data)

