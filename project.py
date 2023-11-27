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

    def show_task(self, nazvanie):
        for i in self.tasks:
            if i['nazvanie'] == nazvanie:
                print(i['opisanie'])
                print(i['task_date'])
            else: print ('there is no such task')

    def del_task (self, nazvanie):
        for i in self.tasks:
            if i['nazvanie'] == nazvanie:
                del self.tasks['nazvanie']
                del self.tasks['opisanie']
                del self.tasks['task_date']
            else: print ('there is no such task')



d= ToDoList()
d.add_task('ghf','fghj','12.04.2023')
d.show_task('ghf')
d.del_task('ghf')

