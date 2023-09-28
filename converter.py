from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        feet_value = float(feets.get())
        meters.set(feet_value * 0.0348)
    except:
        pass

root = Tk()
root.title('Feets to Meters')

mainFrame = ttk.Frame(root,  padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feets = StringVar()
feet_entry = ttk.Entry(mainFrame, width=7, textvariable=feets)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainFrame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainFrame, text='Calculate', command=calculate).grid(column=3, row=3, sticky=E)

ttk.Label(mainFrame, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainFrame, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainFrame, text="meters").grid(column=3, row=2, sticky=W)


# Pour chaque widget, ajouter du padding
for child in mainFrame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
# Au démarrage, forcer le cursor à se retrouver dans la zone de saisie
feet_entry.focus()
# Associer la touche return à la fonction calculate
root.bind("<Return>", calculate)

root.mainloop()