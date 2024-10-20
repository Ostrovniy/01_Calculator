import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class CalculatorFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Настроука сетки для внопок и поля вводе
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')

        # Поле ввода выражения и отображения результата
        self.entry_str = tk.StringVar()
        self.entry = ttk.Entry(self, textvariable=self.entry_str)
        self.entry.grid(row=0, column=0, columnspan=5, sticky='wnes')

        # Кнопка стереть последний введенный символ
        self.back = ttk.Button(self, text='<')
        self.back.grid(row=1, column=0, sticky='wnes')

        # Кнопка расчитать процент
        self.percent = ttk.Button(self, text='%')
        self.percent.grid(row=1, column=1, sticky='wnes')

        # Кнопка очистить поле ввода
        self.reset = ttk.Button(self, text='c')
        self.reset.grid(row=1, column=2, sticky='wnes')

        # Кнопка сложыть "+"
        self.addition = ttk.Button(self, text='+')
        self.addition.grid(row=1, column=3, sticky='wnes')

        # Кнопка 7
        self.seven = ttk.Button(self, text='7')
        self.seven.grid(row=2, column=0, sticky='wnes')

        # Кнопка 8
        self.eight = ttk.Button(self, text='8')
        self.eight.grid(row=2, column=1, sticky='wnes')

        # Кнопка 9
        self.nine = ttk.Button(self, text='9')
        self.nine.grid(row=2, column=2, sticky='wnes')

        # Кнопка минус "-"
        self.minus = ttk.Button(self, text='-')
        self.minus.grid(row=2, column=3, sticky='wnes')

        # Кнопка 4
        self.four = ttk.Button(self, text='4')
        self.four.grid(row=3, column=0, sticky='wnes')

        # Кнопка 5
        self.five = ttk.Button(self, text='5')
        self.five.grid(row=3, column=1, sticky='wnes')

        # Кнопка 6
        self.six = ttk.Button(self, text='6')
        self.six.grid(row=3, column=2, sticky='wnes')

        # Кнопка деление "/"
        self.division = ttk.Button(self, text='/')
        self.division.grid(row=3, column=3, sticky='wnes')

        # Кнопка 1
        self.one = ttk.Button(self, text='1')
        self.one.grid(row=4, column=0, sticky='wnes')

        # Кнопка 2
        self.two = ttk.Button(self, text='2')
        self.two.grid(row=4, column=1, sticky='wnes')

        # Кнопка 3
        self.three = ttk.Button(self, text='3')
        self.three.grid(row=4, column=2, sticky='wnes')

        # Кнопка умножение "*"
        self.multiplication = ttk.Button(self, text='*')
        self.multiplication.grid(row=4, column=3, sticky='wnes')

        # Кнопка 0
        self.zero = ttk.Button(self, text='0')
        self.zero.grid(row=5, column=0, columnspan=2, sticky='wnes')

        # Кнопка точка "."
        self.point = ttk.Button(self, text='.')
        self.point.grid(row=5, column=2, sticky='wnes')

        # Кнопка равно "="
        self.equals = ttk.Button(self, text='=')
        self.equals.grid(row=5, column=3, sticky='wnes')

        
