import tkinter as tk
root=tk.Tk()
root.geometry("400x400")



def on_checkboks():
    if var.get ==1:
        res_label.config(text = 'нажата')
    else:
        res_label.config(text = 'не нажата')

var = tk.IntVar()
checkbut= tk.Checkbutton(root, text = "Push", variable=var, command=on_checkboks)
checkbut.pack()
res_label = tk.Label(root, text = ' ')
res_label.pack()

root.mainloop()