from tkinter import *
import customtkinter
from Frame.MenuFrame import MenuFrame
from Frame.MainFrame import MainFrame

# Set the theme and color options
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Restaurant Management')
        self.geometry("{}x{}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        self.menu_frame = MenuFrame(master=self)
        self.main_frame = MainFrame(master=self)



# Define app and create app mainloop
app = App()
app.mainloop()
