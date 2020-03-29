from tkinter import *
from controller import TrondelagController
        
class Page:
    def __init__(self, root=None):
        self.frame = Frame(
            root, bg='black')
        self.frame.pack_propagate(0)
        self.frame.pack(fill=BOTH, expand=1)

class TrondheimPage(Page):
    def __init__(self, master):
        Page.__init__(self)
        self.controller = TrondelagController()
        self.__set_layout()
        
    def __city_info(self, name=None, rank=0):
        city_data = self.controller.city_data(name=name, rank=rank)
        
        name = city_data['navn']
        name_label = Label(
            self.frame, text=name, fg='white', bg='black',
            font=("Helvetica",50),
            )
        name_label.pack()
        
        infected = city_data['smittet']
        dead = city_data['dode']
        stats_label = Label(
            self.frame,
            text="{}/{}".format(infected,dead),
            fg='white', bg='black',
            font=("Helvetica",100)
            )
        stats_label.pack()
         

    def __set_layout(self):
        self.__city_info('Trondheim')
        
        last_update = self.controller.last_updated()
        update_label = Label(
            self.frame, text=last_update.strftime("%H:%M:%S"),
            fg='white', bg='black',
            font=("Helvetica",30)
            )
        update_label.pack(side=BOTTOM)

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
        dead = city_data['dode']
        stats_label = Label(
            self.frame, text="{}/{}".format(infected,dead)
            )
        stats_label.pack()
        

        
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
        
        self.button = Button(
            self.frame, text='QUIT', fg="red", command=self.frame.quit
            )
        self.button.pack(side=LEFT)
        
        self.top_cases_button = Button(
            self.frame, text='Top Cases', command=self.__top_cases
            )
        self.top_cases_button.pack(side=LEFT)
        
        self.trondheim_button = Button(
            self.frame, text='Trondheim', command=self.__trondheim
            )
        self.trondheim_button.pack(side=LEFT)
        
    def __top_cases(self):
        top_cases = TopCasesPage(self.frame.master)
        self.frame.destroy()
    
    def __trondheim(self):
        trondheim = TrondheimPage(self.frame.master)
        self.frame.destroy()

class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("COVID-19 // TRD")
        landing_page = LandingPage(self.root)
        self.root.mainloop()
        
app=App()
