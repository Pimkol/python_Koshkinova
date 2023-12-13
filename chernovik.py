import tkinter as tk
root=tk.Tk()
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack (padx=10,pady=10)


def on_checkboks():
    if var.get == 1:
        res_label.config(text = 'нажата 1 ')
    elif var.get == 2:
         res_label.config(text = 'нажата 2 ')
    else:
        res_label.config(text = 'нажата 3')

var = tk.IntVar()
checkbut1= tk.Checkbutton(frame, text = "1", variable=var, command=on_checkboks)
checkbut1.pack()
checkbut2= tk.Checkbutton(frame, text = "2", variable=var, command=on_checkboks)
checkbut2.pack()
checkbut3= tk.Checkbutton(frame, text = "3", variable=var, command=on_checkboks)
checkbut3.pack()

res_label = tk.Label(root, text = ' ')
res_label.pack()

root.mainloop()




    


