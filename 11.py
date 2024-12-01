from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter.ttk import Radiobutton
from tkinter import Menu
from tkinter import filedialog
#Главное окно
window=Tk()
window.title('Гонтарь Владислав')
window.geometry('1000x500')
#Функция калькулятора
def CALC():
    try:
        a=float(calc_number_1.get())
        b=float(calc_number_2.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Неккоректные значения')
    else:
        r=calc.get()
        if r=='+':
            s=a+b
            lbl_calc.configure(text=f'={s}')
        elif r=='-':
            s=a-b
            lbl_calc.configure(text=f'={s}')
        elif r=='*':
            s=a*b
            lbl_calc.configure(text=f'={s}')
        elif r=='/':
            try: 
                s=a/b
            except ZeroDivisionError:
                messagebox.showerror('Ошибка', 'Ошибка деления на ноль')
            else: 
                lbl_calc.configure(text='={}'.format(s))
        else:
            messagebox.showwarning('Ошибка', 'Действие не определено')
#Функция чекбоксов
def VAR():
    messagebox.showinfo('Позрдравляем!', 'Вы выбрали {} вариант'.format(sel.get()))
#Фунция для загрузки текстового файла
def DOWNLOAD():
    file=filedialog.askopenfilename(filetypes=(("Text files","*.txt"),("all files","*.*")))
    with open(file, 'r') as txt:
        for line in txt:
            text_box.delete(1.0, END)
            text_box.insert(1.0, line)
#Управление вкладками
Tab=ttk.Notebook(window)
#Вкладка с калькутятором
tab_calc=ttk.Frame(Tab)
Tab.add(tab_calc, text='Калькулятор', padding=5)
Tab.pack(expand=1, fill='both')
#Поля для ввода
calc_number_1=Entry(tab_calc, width=10, font=('Arial Bold', 10))
calc_number_1.grid(column=0, row=0)
calc_number_2=Entry(tab_calc, width=10, font=('Arial Bold', 10))
calc_number_2.grid(column=2, row=0)
#Список действий
calc=Combobox(tab_calc, width=2)
calc.grid(column=1, row=0)
calc['values']=('+', '-', '*', '/')
#Результат калькулятора
lbl_calc=Label(tab_calc, text='=', anchor=W)
lbl_calc.grid(column=3, row=0)
#Кнопка для произведения вычислений
btn_calc=Button(tab_calc, text='Посчитать', command=CALC)
btn_calc.grid(column=0, row=1)
#Вкладка с чекбоксами
tab_check=ttk.Frame(Tab)
Tab.add(tab_check, text='Чекбоксы', padding=5)
Tab.pack(expand=1, fill='both')
#Чекбоксы
sel=IntVar()
rad1 = Radiobutton(tab_check, text='Первый', value=1, command=VAR, variable=sel)
rad2 = Radiobutton(tab_check, text='Второй', value=2, command=VAR, variable=sel)
rad3 = Radiobutton(tab_check, text='Третий', value=3, command=VAR, variable=sel)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
#Вкладка с текстом
tab_text=ttk.Frame(Tab)
Tab.add(tab_text, text='Текст', padding=5)
Tab.pack(expand=1, fill='both')
#Меню для загрузки
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Загрузить', command=DOWNLOAD)
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
#Текстовое поле
text_box=Text(tab_text, font=('Arial Bold', 15), wrap=WORD)
text_box.pack(expand=1, fill='both')
window.mainloop()