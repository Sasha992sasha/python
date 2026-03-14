class Task:
    def __init__(self,name,dedline,deskr):
        self.name = name
        self.dedline = dedline
        self.deskr = deskr

class TaskMBR:
    def __init__(self):
        self.tasks = []
        try:
            with open("task.txt" , "r")as f:
                for i in f:
                    i.strip()
                    name,dedline,deskr = i.strip().split(' | ')
                    self.tasks.append(Task(name,dedline,deskr))
        except:
            print("Нема твоїх завдань(")
            a = open("task.txt" , "w")
    
    def save_file(self):
        
        with open ("task.txt" , 'w') as f:
            for i in self.tasks:
                f.write(f"{i.name} | {i.dedline} | {i.deskr}")
    
    def add(self,file):
        self.tasks.append(file)
        self.save_file

    def print_task(self):
        for i in self.tasks:
            print(f"{i.name} {i.dedline} {i.deskr}")

MBR = TaskMBR()


a = input('Введи назву ')
b = input('Введи дедлайн')
c = input('Введи опис ')

d = Task(a , b , c)

MBR.add(d)
MBR.save_file()
MBR.print_task()
