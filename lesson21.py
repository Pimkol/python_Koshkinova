import tkinter as tk 


def closeWindow ():
    jacob.configure(text = "Новый текст")

def canvas_click (event):
    x, y = event.x , event.y
    jacob.configure( text = f"Click on {x},{y}" )

window = tk.Tk()
window.title("First window")
window.geometry ("800x600")

troi = tk.Canvas(window, width=300, height=300, bg= '#9dc1b4')
lucy = tk.Button(window, text="Стереть текст")
jacob = tk.Label(window, text="Текс для очищения")

lucy.config(command=closeWindow)
troi.bind("<Button-1>", canvas_click)

troi.pack()
lucy.pack()
jacob.pack()

window.mainloop()