import tkinter as tk
from tkinter import ttk
root =tk.Tk()
root.title('Домашка по лекции 23')
root.geometry("400x400")

def button_click ():
    selected_item = combo.get()
    label.config(text = selected_item)


frame1 = tk.Frame(root)
frame1.pack()
values = ['выбор1','выбор2','выбор3']
combo = ttk.Combobox(frame1,  values=values )
combo.pack()

button= tk.Button(frame1,text = 'Выбор', command= button_click)
button.pack()

label= tk.Label(frame1,text= 'Hello')
label.pack()

selected_item = combo.get()
combo.bind("<<ComboboxSelected>>", button_click)
root.mainloop()