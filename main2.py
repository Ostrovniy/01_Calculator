import tkinter as tk
from tkinter import ttk
from module.simple_calculator.calculator import CalculatorFrame

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Calculator')
        self.geometry('900x600')
        self.option_add("*tearOff", tk.FALSE)

        tk.Label(self, text='Test').pack()
        CalculatorFrame(self).pack()



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
