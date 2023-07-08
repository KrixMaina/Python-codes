import customtkinter
import tkinter
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x800")
root.title("HACK WORLD")
img = (Image.open('Password-Hacker_adobespark-2.png'))

li = customtkinter.CTkLabel(root,width=450,height=450,image=img)
li.pack()
root.mainloop()