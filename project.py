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
            print("No tasks found.")
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

    def edit_task(self, task_num, new_nazvanie, new_opisanie):
        if task_num < 1 or task_num > len(self.tasks):
            print("Invalid task number.")
        else:
            task = self.tasks[task_num - 1]
            task.nazvanie = new_nazvanie
            task.description = new_opisanie

    def menu(self):
        print("===== Menu =====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Edit task")
      

    def run(self):
        while True:
            self.menu()
            choice = input("Enter NUMBER: ")
            if choice == "1":
                self.show_task()
            elif choice == "2": 
                nazvanie = input("Enter task title: ")
                opisanie = input("Enter task description: ")
                task_date= input("Enter task date: ")
                self.add_task(nazvanie, opisanie,task_date)
                print("Task added successfully.")
            elif choice == "3":
                index = int(input("Enter task index to remove: ")) - 1
                self.remove_task(index)
                print("Task removed successfully.")
            elif choice == "4":
                index = int(input("Enter task index to edit: ")) - 1
                title = input("Enter new task title: ")
                description = input("Enter new task description: ")
                self.edit_task(index, title, description)
                print("Task edited successfully.")
            else:
                print("Нет такого пункта")


d= ToDoList()
d.run()

