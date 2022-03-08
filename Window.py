#import tkinter
from tkinter import *
from tkinter import ttk
from tokenize import String
from turtle import st # Newer widgets

#------------------FUNCTIONS------------------
def updateChoice(*args):
    value = funcs.get()
    if value == 0:
        print("Gradient line")
    elif value == 1:
        print("Gradient circle")
    elif value == 2:
        print("Gradient Spiral")
    else:
        print("Gradient idek how you got this")

#-------------------WINDOW--------------------
root = Tk()
root.title('Gradient Support Designer')

root.minsize(250, 400)
##  Create a frame to store the widgets in to theme it
mainframe = ttk.Frame(root)
mainframe.grid(sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

##  Apply dark theme to window
root.tk.call('source', 'Azure-ttk-theme-2.1.0/azure.tcl')
root.tk.call('set_theme', 'dark')

s = ttk.Style()
##  Create radio buttons for different modes
s.configure('SidebarBackground.TFrame', background='#242424')
s.configure('SidebarBackground.TRadiobutton', background='#242424')

funcframe = ttk.Frame(mainframe, padding=(3, 3, 12, 12), style='SidebarBackground.TFrame', width=250)
funcframe.grid(row=0, column=0, sticky='nsew')

funcframe.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(0, weight=1)
mainframe.grid_rowconfigure(0, weight=1)

funcs = IntVar()
funcs_b1 = ttk.Radiobutton(funcframe, text='Gradient Line', command=updateChoice, variable=funcs, value=0, style='SidebarBackground.TRadiobutton').grid(column=0, row=0, sticky=W)
funcs_b2 = ttk.Radiobutton(funcframe, text='Gradient Circle [Not supported]', command=updateChoice, variable=funcs, state=DISABLED, value=1, style='SidebarBackground.TRadiobutton').grid(row=1, sticky=W)
funcs_b3 = ttk.Radiobutton(funcframe, text='Gradient Spiral [Not supported]', command=updateChoice, variable=funcs, state=DISABLED, value=2, style='SidebarBackground.TRadiobutton').grid(row=2, sticky=W)

## Start the event loop
root.mainloop()
