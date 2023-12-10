import tkinter as tk
def button_click(event):
    text = entry.get()
    label.config(text="Hello")

window=tk.Tk()
window.geometry('400x400')

entry=tk.Entry(window)
entry.pack()
entry.bind("<Return>",button_click )

label = tk.Label(window, text="привет")
label.pack()

button = tk.Button(window,text = "Нажми")
button.pack()
window.mainloop()