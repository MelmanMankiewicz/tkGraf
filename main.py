#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import filedialog
import pylab as pl

# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Siuuuuuu"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="tkGraf")
        self.lbl.pack()

        self.fileFrame = tk.LabelFrame(self, text="Soubor")
        self.fileFrame.pack(padx=5, pady=5, fill='x')
        self.fileEntry = MyEntry(self.fileFrame)
        self.fileEntry.pack(fill="x")
        self.fileBtn = tk.Button(self.fileFrame, text="...", command=self.fileSelect)
        self.fileBtn.pack(anchor="e")
        
        self.dataformatVar = tk.StringVar(value="RADEK")
        self.radkyRbtn = tk.Radiobutton(
            self.fileFrame,
            text="Data jsou v řádcích",
            variable=self.dataformatVar,
            value="RADEK",
        )
        self.radkyRbtn.pack(anchor="w")
        self.sloupceRbtn = tk.Radiobutton(
            self.fileFrame,
            text="Data jsou ve sloupcích",
            variable=self.dataformatVar,
            value="SLOUPEC",
        )
        self.sloupceRbtn.pack(anchor="w")

        self.grafFrame = tk.LabelFrame(self, text="Graf")
        self.grafFrame.pack(padx=5, pady=5, fill='x')
        tk.Label(self.grafFrame, text="Titulek").grid(row=0, column=0)
        self.titleEntry = MyEntry(self.grafFrame)
        self.titleEntry.grid(row=0, column=1)
        tk.Label(self.grafFrame, text="popisek X").grid(row=1, column=0)
        self.xlabelEntry = MyEntry(self.grafFrame)
        self.xlabelEntry.grid(row=1, column=1)
        tk.Label(self.grafFrame, text="popisek Y").grid(row=2, column=0)
        self.ylabelEntry = MyEntry(self.grafFrame)
        self.ylabelEntry.grid(row=2, column=1)

        tk.Label(self.grafFrame, text="mřížka").grid(row=3, column=0)
        self.gridVar = tk.BooleanVar(value=False)
        self.gridChck = tk.Checkbutton(self.grafFrame, variable=self.gridVar)
        self.gridChck.grid(row=3, column=1, sticky="w")
        
        tk.Label(self.grafFrame, text="Styl čáry").grid(row=4, column=0)
        self.lineVar = tk.StringVar(value='none') 
        self.lineOpt = tk.OptionMenu(self.grafFrame, self.lineVar, 'none', '-', '--', ':', '-.')
        self.lineOpt.grid(row=4, column=1, sticky='w')

        tk.Button(self, text="Kreslit", command=self.plotgraph).pack(anchor='w')
        tk.Button(self, text="Quit", command=self.quit).pack(anchor='e')

    def fileSelect(self):
        self.filename = filedialog.askopenfilename()
        self.fileEntry.value = self.filename

    def plotgraph(self):
        with open(self.filename, "r") as f:
            if self.dataformatVar.get() == "RADEK":
                x = f.readline().split(";")
                y = f.readline().split(";")
                x = [float(i.replace(",", ".")) for i in x]
                y = [float(i.replace(",", ".")) for i in y]
            elif self.dataformatVar.get() == "SLOUPEC":
                x = []
                y = []
                while True:
                    line = f.readline()
                    if line == '':
                        break
                    x1, y1 = line.split()
                    x1 = float(x1.replace(",", "."))
                    y1 = float(y1.replace(",", "."))
                    x.append(x1)
                    y.append(y1)

        pl.plot(x,y, 'o', linestyle=self.lineVar.get())
        pl.title(self.titleEntry.value)
        pl.xlabel(self.xlabelEntry.value)
        pl.ylabel(self.ylabelEntry.value)
        pl.grid(self.gridVar.get())
        pl.show()
        

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
