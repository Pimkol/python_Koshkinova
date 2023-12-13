import tkinter as tk

def bold_button ():
    text.tag_add('bold', text.index(tk.SEL_FIRST),text.index(tk.SEL_LAST))
    text.tag_config("bold",font = ("Times New Roman", 14 , 'bold'))
    
window=tk.Tk()
window.geometry('400x400')

button = tk.Button(window,text = "Сделать жирным", command=bold_button )
button.pack()
text = tk.Text(window, height= 30, width=50)
text.pack()
window.mainloop()

#2
def bold_button ():
    text.tag_add('bold', text.index(tk.SEL_FIRST),text.index(tk.SEL_LAST))
    text.tag_config("bold",font = ("Times New Roman", 14 , 'bold'))
    text_conten=text.get("1.0", "end")
    label.config(text=text_conten)
window=tk.Tk()
window.geometry('400x400')

button = tk.Button(window,text = "Сделать жирным", command=bold_button )
button.pack()

text = tk.Text(window, height= 10, width=10)
text.pack()

label = tk.Label(window, text="Hello ")
label.pack()
window.mainloop()