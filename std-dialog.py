import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


# messagebox.showwarning('Warování', 'Sorry, error!')
# bagr = messagebox.askyesnocancel('titule', 'Jak se dnes máš?')
# print(bagr)

bagr = filedialog.askdirectory('Vyber složku')
print(bagr)