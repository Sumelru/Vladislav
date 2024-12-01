import requests
from requests.exceptions import HTTPError
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window=Tk()
window.title('Гонтарь Владислав')
window.geometry('1000x500')

def clicked():
    url=f'https://api.github.com/users/{vvod.get()}'
    try:
        response=requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        messagebox.showerror('Ошибка', f'HTTP error occurred: {http_err}')
    except Exception as err:
        messagebox.showerror('Ошибка', f'Other error occurred: {err}')
    else:
        with open('12.3/Result.txt', 'w') as result:
            user_data=requests.get(url).json()
            result.writelines(f'company: {str(user_data.get('company'))}\n')
            result.writelines(f'created_at: {str(user_data.get('created_at'))}\n')
            result.writelines(f'email: {str(user_data.get('email'))}\n')
            result.writelines(f'id: {str(user_data.get('id'))}\n')
            result.writelines(f'name: {str(user_data.get('name'))}\n')
            result.writelines(f'url: {str(user_data.get('url'))}')
        messagebox.showinfo('Выполнено', f'Данные сохранены в файл: {os.path.abspath('12.3/Result.txt')}')

lbl=Label(window, text='Введите имя: ', anchor=W, font=('Arial Bold', 15))
lbl.grid(column=0, row=0)

vvod=Entry(window, width=30, font=('Arial Bold', 15))
vvod.grid(column=1, row=0)

btn=Button(window, text='Получить данные', command=clicked)
btn.grid(column=2, row=0)

window.mainloop()