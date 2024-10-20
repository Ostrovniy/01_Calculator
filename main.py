from tkinter import *
from tkinter import ttk

"""

Калькулятор который принимает значения с кнопок и передает данные в поле ввода, 
кнопка равно производит расчет уравнения функцыей eval, кнопка % не работает, 
в случаее ошибки, отображаеться текст "Ошибка при нажатии на кнопку равно
история записываеться в таблицу, максимум доступно последние 19 записей

"""

root = Tk()
root.title("METANIT.COM")
root.geometry("900x400")
root.resizable(False, False)  # (ширина, высота) # Запрет изменения размера окна

counter = 1 # Щетчик истории

# Обработка кнопок 0-9 и +-*/
def add_number(value):
    text_input = input_entry.get() # Текущий текст в поле
    #print(text_input)
    input_entry.insert(END, value)

# Обработка кнопки Сброс
def reset_input():
    input_entry.delete(first=0, last=END)

# Обработка кнопки "ШагНазад"
def step_back():
    text_input = input_entry.get()  # Получаем текущий текст
    if len(text_input) > 0:  # Проверяем, что текст не пустой
        input_entry.delete(len(text_input) - 1, END)  # Удаляем последний символ

# Обработка кнопки Равно
def ravno():
    text_input = input_entry.get() # Текущий текст в поле
    reset_input()
    try:
        global counter
        res = eval(text_input) # Результат вычисления
        input_entry.insert(0, res) # Запись результата в компонент вывода
        history_table.insert("", END, values=(str(counter), text_input, str(res)))
        counter+=1
        children = history_table.get_children() # Получить данные с таблицы
        if len(children) >= 19:
            history_table.delete(children[0]) # Удалить первую строку


    except:
        input_entry.insert(0, 'Ошибка')


# Фрейм для Калькулятора, в котормо находяться кнопки и полве ввода
kal_frame = ttk.Frame(borderwidth=2, relief=SOLID, padding=[10, 6], height=400, width=300)
kal_frame.grid(row=0, column=0, sticky='nw')
kal_frame.grid_propagate(False) # Запрет изменения размера фрейма в зависимости от содержимого

# Фрейм для Калькулятора, изменения размера строк и колонок
for c in range(3): kal_frame.columnconfigure(index=c, weight=60, uniform="equal_columns", minsize=60)
for r in range(6): kal_frame.rowconfigure(index=r, weight=80, uniform="equal_rows")

# Фрейм для Истории Калькулятора в котором находиться таблица истории
history_frame = ttk.Frame(borderwidth=2, relief=SOLID, padding=[10, 6], height=400, width=600)
history_frame.grid(row=0, column=1, sticky='nw')
history_frame.grid_propagate(False) # Запрет изменения размера фрейма в зависимости от содержимого

# Поле ввода ИНПУТ
input_entry = ttk.Entry(master=kal_frame, justify='right', font=('Arial', 15))
input_entry.grid(column=0, row=0, columnspan=5, sticky='nsew', ipadx=4, ipady=4, pady=4)

# Кнопки от 0 до 9 + . (Фрейм для Калькулятора)
for i in range(9):
    row_set = [2, 2, 2, 3, 3, 3, 4, 4, 4]
    column_set = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    number_set = [7, 8 , 9, 4, 5, 6, 1, 2, 3]
    number = number_set[i]
    btn = ttk.Button(master=kal_frame, text=f'{number}', command=lambda numb = number: add_number(numb))
    btn.grid(column=column_set[i], row=row_set[i], sticky='nsew')
else:
    btn_0 = ttk.Button(master=kal_frame, text='0', command=lambda: add_number('0'))
    btn_0.grid(column=0, row=5, columnspan=2, sticky='nsew')
    btnpoint = ttk.Button(master=kal_frame, text='.', command=lambda: add_number('.'))
    btnpoint.grid(column=2, row=5, sticky='nsew')

# Кнопки Математические операции + - / * = % очистить (Фрейм для Калькулятора)
for i in range(4):
    row_set = [1, 2, 3, 4]
    column_set = [3, 3, 3, 3]
    text_set = ['+', '-', '/', '*']
    operatsion = text_set[i]
    # Исправляем lambda, добавляя параметр по умолчанию для фиксации значения operatsion
    btn_op = ttk.Button(master=kal_frame, text=operatsion, command=lambda oper=operatsion: add_number(oper))
    btn_op.grid(column=3, row=row_set[i], sticky='nsew')
else:
    # Кнпка равно
    btn_ravno = ttk.Button(master=kal_frame, text='=', command=ravno)
    btn_ravno.grid(column=3, row=5, sticky='nsew')
    # Кнопка очистить поле ввода
    btn_c = ttk.Button(master=kal_frame, text='c', command=reset_input)
    btn_c.grid(column=2, row=1, sticky='nsew')
    # Кнопка процента
    btn_procent = ttk.Button(master=kal_frame, text='%', command=lambda : add_number('%'))
    btn_procent.grid(column=1, row=1, sticky='nsew')
    # Стереть последний символ 🔙
    btn_step_back = ttk.Button(master=kal_frame, text='<', command=step_back)
    btn_step_back.grid(column=0, row=1, sticky='nsew')


# Создание таблицы истории (Фрейм для История Калькулятора)
name_column = ('№', 'Выражение', 'Результат')
history_table =  ttk.Treeview(master=history_frame, column=name_column, show='headings', height=18)
history_table.grid(column=1, row=0, rowspan=2, sticky='nw')

# Настройка заголовков таблицы
history_table.heading('№', text='№')
history_table.column('№', width=50, anchor='w')
history_table.heading('Выражение', text='Выражение')
history_table.column('Выражение', width=375, anchor='w')
history_table.heading('Результат', text='Результат')
history_table.column('Результат', width=150, anchor='w')

root.mainloop()