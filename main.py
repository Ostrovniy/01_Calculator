import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from module.simple_calculator.calculator import CalculatorFrame

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.style_them = ttk.Style("darkly")

        self.title('Calculator')
        self.geometry('900x600')
        self.themename="darkly"
        self.option_add("*tearOff", tk.FALSE)

        CalculatorFrame(self).pack(anchor='nw')



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
