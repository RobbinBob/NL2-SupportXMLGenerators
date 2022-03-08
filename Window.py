#import tkinter
from tkinter import *
from tkinter import ttk # Newer widgets

#------------------FUNCTIONS------------------
def calculate(*args):
    try:
        value = float(textEntry.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass

#-------------------WINDOW--------------------
root = Tk()
root.title('Gradient Support Designer')

##  Create a frame to store the widgets in to theme it
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.tk.call('source', 'Azure-ttk-theme-2.1.0/azure.tcl')
root.tk.call('set_theme', 'dark')

##  Create entry widget
textEntry = StringVar()
textEntry_entry = ttk.Entry(mainframe, width=7, textvariable=textEntry)
textEntry_entry.grid(column=2, row=1, sticky=(W, E))

##  Create label widget
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

##  Create button widget
ttk.Button(mainframe, text='Calculate', command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
textEntry_entry.focus()

##  Bind the return key to calculate function
root.bind('<Return>', calculate)

## Start the event loop
root.mainloop()
