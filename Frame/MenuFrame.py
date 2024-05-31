import customtkinter
from Frame.BaseFrame import BaseFrame


class MenuFrame(BaseFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, fg_color='#969292')
        self.label.pack(expand=True, fill='both')
        self.place(x=0, y=0, relwidth=0.25, relheight=1)
