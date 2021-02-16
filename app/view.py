from tkinter import *
from controller import TrondelagController, HelsedirController
        
class Page:
    def __init__(self, root=None):
        self.frame = Frame(
            root, bg='black')
        self.frame.pack_propagate(0)
        self.frame.pack(fill=BOTH, expand=1)

class HelsedirPage(Page):
    def __init__(self, master):
        Page.__init__(self)
        self.controller_stOlavs = HelsedirController("helseforetak")
        self.controller_national = HelsedirController()
        self.__set_layout()

    def __stats(self):
        hospitalized_stOlavs = self.controller_stOlavs.hospitalized()
        hospitalized_national = self.controller_national.hospitalized()
        
        name = "COVID-19"
        name_label = Label(
            self.frame, text=name, fg='white', bg='black',
            font=("Helvetica",110),
            )
        name_label.place(relx=0.5,rely=0.15,anchor='center')
        
        self.stats_label = Label(
            self.frame,
            text="{}/{}".format(hospitalized_national,hospitalized_stOlavs),
            fg='white', bg='black',
            font=("Helvetica",290)
            )
        self.stats_label.place(relx=0.5,rely=0.5,anchor='center')

    def __set_layout(self):
        self.__stats()
        last_update = self.controller_stOlavs.last_updated()
        self.update_label = Label(
            self.frame, text=last_update.strftime("%H:%M"),
            fg='white', bg='black',
            font=("Helvetica",100)
            )
        self.update_label.place(relx=0.5,rely=0.9,anchor='center')
        self.__update_info()

    def __update_info(self):
        self.controller_stOlavs.update_model()
        self.controller_national.update_model()

        hospitalized_stOlavs = self.controller_stOlavs.hospitalized()
        hospitalized_national = self.controller_national.hospitalized()
        self.stats_label.configure(text="{}/{}".format(hospitalized_national,hospitalized_stOlavs))
        
        
        last_update = self.controller_stOlavs.last_updated()
        self.update_label.configure(text=last_update.strftime("%H:%M"))
        
        self.stats_label.after(60000, lambda: self.__update_info())

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
            font=("Helvetica",110),
            )
        name_label.place(relx=0.5,rely=0.15,anchor='center')
        
        infected = city_data['smittet']
        dead = city_data['dode']
        self.stats_label = Label(
            self.frame,
            text="{}/{}".format(infected,dead),
            fg='white', bg='black',
            font=("Helvetica",290)
            )
        self.stats_label.place(relx=0.5,rely=0.5,anchor='center')

    def __set_layout(self):
        self.__city_info('Trondheim')
        last_update = self.controller.last_updated()
        self.update_label = Label(
            self.frame, text=last_update.strftime("%H:%M:%S"),
            fg='white', bg='black',
            font=("Helvetica",100)
            )
        self.update_label.place(relx=0.5,rely=0.9,anchor='center')
        self.__update_info('Trondheim')
        
    def __update_info(self, name=None, rank=0):
        self.controller.update_model()
        city_data = self.controller.city_data(name=name, rank=rank)
        
        infected = city_data['smittet']
        dead = city_data['dode']
        self.stats_label.configure(text="{}/{}".format(infected,dead))
        
        
        last_update = self.controller.last_updated()
        self.update_label.configure(text=last_update.strftime("%H:%M:%S"))
        
        self.stats_label.after(30000, lambda: self.__update_info(name=name,rank=rank))

class App():
    def __init__(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        self.root.config(cursor="none")
        self.root.title("COVID-19")
        landing_page = HelsedirPage(self.root)
        self.root.mainloop()
        