import tkinter as tk
from tkinter import ttk

class CalculatorFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text='Frame Cal').pack()