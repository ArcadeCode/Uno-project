from tkinter import *
from tkinter import ttk
root = Tk()
frm_title = ttk.Frame(root, padding=100)

frm_title.pack(side="top")

root.title("Uno en python | Page d'acceuil")
root.maxsize(400, 200)


ttk.Label(frm_title, text="Uno in python").grid(column=0, row=0)

ttk.Button(frm_title, text="Créer une partie").grid(column=0, row=1)
ttk.Button(frm_title, text="Charger une partie").grid(column=0, row=2)

ttk.Button(frm_title, text="Options").grid(column=1, row=3)
ttk.Button(frm_title, text="Quiter", command=root.destroy).grid(column=0, row=3)

root.mainloop()