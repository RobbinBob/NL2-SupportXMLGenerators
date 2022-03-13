#import tkinter
from generators import *

from tkinter import *
from tkinter import ttk
import sys
import os

from generators.GradientLine import GradientLine

#------------------FUNCTIONS------------------
def updateChoice(*args):
    value = funcs.get()
    if value == 0:
        print("Gradient line")
        #_gradientLine.start()
    elif value == 1:
        print("Gradient circle")
    elif value == 2:
        print("Gradient Spiral")
    else:
        print("Gradient idek how you got this")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
#--------------------DIR----------------------
theme_dir = resource_path('themes')

#-------------------WINDOW--------------------
root = Tk()
root.title('Gradient Support Designer')

root.minsize(700, 400)
##  Create a frame to store the widgets in to theme it
mainframe = ttk.Frame(root)
mainframe.grid(sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

##  Apply dark theme to window
root.tk.call('source', os.path.join(theme_dir, 'azure.tcl'))
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
mainframe.grid_columnconfigure(1, weight=1)

funcs = IntVar()
funcs_b1 = ttk.Radiobutton(funcframe, text='Gradient Line', command=updateChoice, variable=funcs, value=0, style='SidebarBackground.TRadiobutton').grid(column=0, row=0, sticky=W)
funcs_b2 = ttk.Radiobutton(funcframe, text='Gradient Circle [Not supported]', command=updateChoice, variable=funcs, state=DISABLED, value=1, style='SidebarBackground.TRadiobutton').grid(row=1, sticky=W)
funcs_b3 = ttk.Radiobutton(funcframe, text='Gradient Spiral [Not supported]', command=updateChoice, variable=funcs, state=DISABLED, value=2, style='SidebarBackground.TRadiobutton').grid(row=2, sticky=W)

#--------------------CLASS--------------------
_gradientLine = GradientLine(root, mainframe, s)
_gradientLine.renderOut()

## Start the event loop
root.mainloop()
