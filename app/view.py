from tkinter import *
from controller import TrondelagController

"""

    Remember to update the last_updated as well...
    Move update of model out of view!
"""
        
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
        self.stats_label.after(300000, lambda: self.__update_info(name=name, rank=rank))
    

    def __set_layout(self):
        self.__city_info('Trondheim')
        
        last_update = self.controller.last_updated()
        self.update_label = Label(
            self.frame, text=last_update.strftime("%H:%M:%S"),
            fg='white', bg='black',
            font=("Helvetica",100)
            )
        self.update_label.place(relx=0.5,rely=0.9,anchor='center')
        
    def __update_info(self, name, rank):
        self.controller.update_model()
        city_data = self.controller.city_data(name=name, rank=rank)
        
        infected = city_data['smittet']
        dead = city_data['dode']
        self.stats_label.configure(text="{}/{}".format(infected,dead))
        
        
        last_update = self.controller.last_updated()
        self.update_label.configure(text=last_update.strftime("%H:%M:%S"))
        
        self.stats_label.after(300000, lambda: self.__update_info(name=name,rank=rank))


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
        self.root.attributes("-fullscreen", True)
        self.root.config(cursor="none")
        self.root.title("COVID-19 // TRD")
        landing_page = TrondheimPage(self.root)
        self.root.mainloop()
        