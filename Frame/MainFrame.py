import customtkinter
from Frame.BaseFrame import BaseFrame


class MainFrame(BaseFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.place(relx=0.25, y=0, relwidth=0.75, relheight=1)