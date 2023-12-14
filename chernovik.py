import tkinter as tk
root=tk.Tk()
root.geometry("400x400")

def handle_checkbox():
    selected_values = []
    for checkbox in checkboxes:
        if checkbox.get():
            selected_values.append(checkbox.сget("text"))
    res_label.config(text = selected_values)



checkboxes = []
values = ["Option 1", "Option 2", "Option 3", "Option 4"]

for value in values:
    checkbox = tk.Checkbutton(root, text=value)
    checkbox.pack()
    checkboxes.append(checkbox)

button = tk.Button(root, text="Нажми", command=handle_checkbox)
button.pack()
res_label = tk.Label(root, text = ' ')
res_label.pack()
root.mainloop()




    


