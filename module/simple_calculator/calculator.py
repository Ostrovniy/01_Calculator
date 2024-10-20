import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class CalculatorFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padx=10, pady=10)

        # Стиль что бы увеличить размер шрифта кнопок
        st = ttk.Style()
        st.configure('my.TButton', font=('Helvetica', 24))

        # Настроука сетки для внопок и поля вводе
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')

        # Поле ввода выражения и отображения результата
        self.entry_str = tk.StringVar()
        self.entry = ttk.Entry(self, textvariable=self.entry_str, font=('Helvetica', 24))
        self.entry.grid(row=0, column=0, columnspan=5, sticky='wnes', pady=5)

        # Кнопка стереть последний введенный символ
        self.back = ttk.Button(self, text='<', style='my.TButton')
        self.back.grid(row=1, column=0, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка расчитать процент
        self.percent = ttk.Button(self, text='%', style='my.TButton')
        self.percent.grid(row=1, column=1, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка очистить поле ввода
        self.reset = ttk.Button(self, text='c', style='my.TButton')
        self.reset.grid(row=1, column=2, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка сложыть "+"
        self.addition = ttk.Button(self, text='+', style='my.TButton')
        self.addition.grid(row=1, column=3, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка 7
        self.seven = ttk.Button(self, text='7', style='my.TButton')
        self.seven.grid(row=2, column=0, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка 8
        self.eight = ttk.Button(self, text='8', style='my.TButton')
        self.eight.grid(row=2, column=1, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка 9
        self.nine = ttk.Button(self, text='9', style='my.TButton')
        self.nine.grid(row=2, column=2, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка минус "-"
        self.minus = ttk.Button(self, text='-', style='my.TButton')
        self.minus.grid(row=2, column=3, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка 4
        self.four = ttk.Button(self, text='4', style='my.TButton')
        self.four.grid(row=3, column=0, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка 5
        self.five = ttk.Button(self, text='5', style='my.TButton')
        self.five.grid(row=3, column=1, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка 6
        self.six = ttk.Button(self, text='6', style='my.TButton')
        self.six.grid(row=3, column=2, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка деление "/"
        self.division = ttk.Button(self, text='/', style='my.TButton')
        self.division.grid(row=3, column=3, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка 1
        self.one = ttk.Button(self, text='1', style='my.TButton')
        self.one.grid(row=4, column=0, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка 2
        self.two = ttk.Button(self, text='2', style='my.TButton')
        self.two.grid(row=4, column=1, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка 3
        self.three = ttk.Button(self, text='3', style='my.TButton')
        self.three.grid(row=4, column=2, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка умножение "*"
        self.multiplication = ttk.Button(self, text='*', style='my.TButton')
        self.multiplication.grid(row=4, column=3, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка 0
        self.zero = ttk.Button(self, text='0', style='my.TButton')
        self.zero.grid(row=5, column=0, columnspan=2, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка точка "."
        self.point = ttk.Button(self, text='.', style='my.TButton')
        self.point.grid(row=5, column=2, sticky='wnes', ipadx=20, ipady=20)

        # Кнопка равно "="
        self.equals = ttk.Button(self, text='=', style='my.TButton')
        self.equals.grid(row=5, column=3, sticky='wnes', ipadx=20, ipady=20)

        
