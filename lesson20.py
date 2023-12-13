import tkinter as tk

def button_click():
    label.config(text="Hello")

window=tk.Tk()
window.geometry('400x400')



label = tk.Label(window, text="привет")
label.pack()

button = tk.Button(window,text = "Нажми", command=button_click )
button.pack()
window.mainloop()

#2
import tkinter as tk

def button_click():
    entry.delete(0, tk.END)

window=tk.Tk()
window.geometry('400x400')

entry =tk.Entry(window)
entry.pack()
button = tk.Button(window,text = "Clear", command=button_click )
button.pack()
window.mainloop()