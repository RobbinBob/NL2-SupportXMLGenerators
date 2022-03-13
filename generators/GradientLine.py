import re
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser as colorbox
import sys
import os
import threading

from matplotlib.pyplot import text, title
from numpy import pad

class GradientLine:


    def __init__(self, root : Tk, main : ttk.Frame, style : ttk.Style):
        self._root = root
        self._style = style
        self._main = main
        print("GL : Assign root")

    def start(gui):
        class Threader(threading.Thread):
            def run(self):
                gui._root.mainloop()
        Threader().start()

    def renderOut(self):
        if not self._root or not self._main or not self._style:
            pass
        
        #   Apply frame overlay
        #self._style.configure('MainWindow.TFrame', background="#00ff00")
        back = ttk.Frame(self._main)
        back.grid(row=0,column=1, stick='nwes')

        title = ttk.Label(back, text='Gradient Line Editor', font=('Segoe', 14, 'bold', 'underline'))
        title.grid(row=0, column=0, padx=5)

        ##  Colour picker
        colorback = ttk.LabelFrame(back, padding=(20, 10), text='Color')
        colorback.grid(row=1, column=0, sticky='nw', padx=5, pady=5)

        def getColor1():
            #v.set(colorbox.askcolor(title='Choose color'))
            color1value = colorbox.askcolor(title='Choose color')
            self._style.configure('color1.TFrame', background=color1value[1])
            color1prev.configure(style='color1.TFrame')

        def getColor2():
            #v.set(colorbox.askcolor(title='Choose color'))
            color2value = colorbox.askcolor(title='Choose color')
            self._style.configure('color2.TFrame', background=color2value[1])
            color2prev.configure(style='color2.TFrame')

        color1value, color2value = None, None
        color1 = ttk.Button(colorback, text='Color 1', command=getColor1)
        color1.grid(row=1, column=0, pady=5)
        color2 = ttk.Button(colorback, text='Color 2', command=getColor2)
        color2.grid(row=2, column=0, pady=5)
        color1prev = ttk.Frame(colorback, width=25, height=25)
        color1prev.grid(row=1, column=1, pady=5, padx=5)
        color2prev = ttk.Frame(colorback, width=25, height=25)
        color2prev.grid(row=2, column=1, pady=5, padx=5)

        def getRes(a, b):
            colorres = colorresinput.get()
            print(a)
            print(b)
            print(colorres)

        colorres = None
        colorresinput = ttk.Scrollbar(colorback, command=getRes, orient='horizontal')
        colorresinput.grid(row=3, column=0, padx=5, pady=5)

        ##  Support params
        ##[[
        # - Resolution
        # ]]




