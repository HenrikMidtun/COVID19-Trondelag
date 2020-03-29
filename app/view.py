from tkinter import *
from controller import TrondelagController
        
class Page:
    def __init__(self, root=None):
        self.frame = Frame(root)
        self.frame.pack()
    
    
class TopCasesPage(Page):
    def __init__(self, master):
        Page.__init__(self)
        self.controller = TrondelagController()
        self.__set_layout()
        
    
    def __city_info(self, name=None, rank=0):
        city_data = self.controller.city_data(name=name, rank=rank)
        
        name = city_data['navn']
        name_label = Label(
            self.frame, text=name
            )
        name_label.pack()
        
        infected = city_data['smittet']
        infected_label = Label(
            self.frame, text="Smittede: {}".format(infected)
            )
        infected_label.pack()
        
        dead = city_data['dode']
        dead_label = Label(
            self.frame, text="Døde: {}".format(dead)
            )
        dead_label.pack()
        

        
    def __set_layout(self):
        header_label = Label(
            self.frame, text="COVID-19 Trøndelag"
            )
        
        self.__city_info(rank=0)
        self.__city_info(rank=1)
        self.__city_info(rank=2)
        
        last_update = self.controller.last_updated()
        update_label = Label(
            self.frame, text=last_update.strftime("%b %d. %Y %H:%M:%S")
            )
        update_label.pack()
        
class LandingPage(Page):
    
    def __init__(self, master):
        Page.__init__(self)
        self.__set_layout()
    
    def __set_layout(self):
        self.label = Label(
            self.frame, text='COVID-19'
            )
        self.label.pack()
        
        self.button = Button(
            self.frame, text='QUIT', fg="red", command=self.frame.quit
            )
        self.button.pack(side=LEFT)
        
        self.top_cases_button = Button(
            self.frame, text='Top Cases', command=self.__top_cases
            )
        self.top_cases_button.pack(side=RIGHT)
        
    def __top_cases(self):
        top_cases = TopCasesPage(self.frame.master)
        self.frame.destroy()

class App():
    def __init__(self):
        self.root = Tk()
        landing_page = LandingPage(self.root)
        self.root.mainloop()
