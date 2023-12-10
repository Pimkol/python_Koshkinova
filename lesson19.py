import tkinter as tk
from tkinter import *
window=tk.Tk()
window.title= "Кнопка Выход"
window.geometry('400x400')
label=tk.Label(window,text='Выход')
label.pack()
button = tk.Button(window,text='Выход',command = lambda: window.destroy())
button.pack()




window.mainloop()



#2
import tkinter as tk
from tkinter import *
window=tk.Tk()
window.title= "Кнопка Выход"
window.geometry('400x400')
label=tk.Label(window,text='Жакенова Назгуль Алихановна')

label.pack()




window.mainloop()
