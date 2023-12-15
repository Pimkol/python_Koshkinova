from sqlalchemy import create_engine, Column, Integer, String,Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
class User(Base):
    __tablename__= 'user'
    id=Column(Integer,Sequence('user_id_seq'), primary_key=True)
    name= Column(String(50))
    age= Column(Integer)

engine= create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)
Session =sessionmaker(bind= engine)
session=Session()
person1 = User (name='Nazik', age = 38)
person2 = User (name='Ascar', age = 39)
session.add_all([person1, person2])
session.commit()

persons = session.query(User).all()
for person in persons:
    print (f"Персона: {person.id}, по имени: {person.name}, возраст {person.age}")



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