import datetime
class ToDoList():
    def __init__(self):
        self.tasks = []

    def add_task (self, nazvanie, opisanie,task_date):
        tasks_n = {
            'nazvanie':nazvanie,
            'opisanie':opisanie,
            'task_date':task_date
        }
        self.tasks.append(tasks_n)

    # def show_task(self):
    #     for i in self.tasks:
    #         if len(self.tasks) == 0:
    #             print("Net sobitia.")
    #     else:
    #         for i  in self.tasks:
    #             print(i)

    def show_task(self):
        if not self.tasks:
            print("Заданий нет, возможно нужно добавить.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"Задание #{index + 1}")
                print(task)
                print()

    # def del_task (self, nazvanie):
    #     for i in self.tasks:
    #         if i['nazvanie'] == nazvanie:
    #             del self.tasks['nazvanie']
    #             del self.tasks['opisanie']
    #             del self.tasks['task_date']
    #         else: print ('there is no such task')

    def remove_task(self, index):
        if index >= 0 and index < len(self.tasks):
            del self.tasks[index]

    def edit_task(self, index, new_nazvanie, new_opisanie, new_date):
        if index < 1 or index > len(self.tasks):
            print("Нет такого задания.")
        else:
            task = self.tasks[index - 1]
            task.nazvanie = new_nazvanie
            task.opisanie = new_opisanie
            task.task_date= new_date
          
    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            file.write(self.tasks)

    def menu(self):
        print("===== Menu =====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Edit task")
        print("5. Save task")

      

    def run(self):
        while True:
            self.menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                self.show_task()
            elif choice == "2": 
                nazvanie = input("Введите название задания: ")
                opisanie = input("Описание: ")
                task_date= input("Дата выполнения: ")
                self.add_task(nazvanie, opisanie,task_date)
                print("Задание успешно добавлено.")
            elif choice == "3":
                index = int(input("Номер какого задания нужно удалить: ")) - 1
                self.remove_task(index)
                print("Удалено успешно.")
            elif choice == "4":
                index = int(input("Номер какого задания нужно исправить?: ")) - 1
                nazvanie = input("Введите новое название: ")
                opisanie = input("введите новое описание задания: ")
                date_n= input ('Введите новую дату')
                self.edit_task(index, nazvanie, opisanie, date_n)
                print("Успешно изменено.")
            elif choice == "5":
                filename = input('Введите название файла')
                self.save_tasks(filename)
            else:
                print("Нет такого пункта")


d= ToDoList()
d.run()

