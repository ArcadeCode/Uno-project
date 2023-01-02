from tkinter import *
from tkinter import ttk, messagebox


def showinfo_informations() :
    messagebox.showinfo("Uno en python", "V.0.1\nMade by Dervaux Esteban\nGithub:xxx")

settings = Tk()
frm_title = ttk.Frame(settings, padding=100)

frm_title.pack(side="top")

settings.title("Uno en python | Paramètre")
settings.maxsize(400, 200)


ttk.Button(frm_title, text="Infos", function=showinfo_informations()).grid(column=0, row=0)

settings.mainloop()