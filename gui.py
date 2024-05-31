from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

font_style = {"font": ("Montserrat", 40, "bold")}

root.title('Restaurant Management')
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

menu_frame = customtkinter.CTkFrame(root)
main_frame = customtkinter.CTkFrame(root)

# main layout widgets
menu_frame.place(x=0, y=0, relwidth=0.25, relheight=1)
main_frame.place(relx=0.25, y=0, relwidth=0.75, relheight=1)

# customtkinter.CTkLabel(menu_frame, text='', fg_color='#969292').pack(expand=True, fill='both')
customtkinter.CTkLabel(main_frame, text='', fg_color='#3b3a39').pack(expand=True, fill='both')

# menu layout
menu_frame.columnconfigure((0,1,2), weight=1)
menu_frame.rowconfigure((0,1,2,3,4), weight=1)

# Menu widgets
menu_button1 = customtkinter.CTkButton(menu_frame, text='Orders', **font_style)
menu_button2 = customtkinter.CTkButton(menu_frame, text='Menu', **font_style)
menu_button3 = customtkinter.CTkButton(menu_frame, text='Revision', **font_style)

# Buttons placed
menu_button1.grid(pady=(40, 20), padx=(50, 0), row=0, column=0, sticky='nswe', columnspan=2)
menu_button2.grid(pady=20, padx=(50, 0), row=1,  column=0, sticky='nswe', columnspan=2)
menu_button3.grid(pady=20, padx=(50, 0), row=2, column=0, sticky='nswe', columnspan=2)

if __name__ == "__main__":
    root.mainloop()