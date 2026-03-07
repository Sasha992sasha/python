class Task:
    def __init__(self,name,opis,dedline,stan):
        self.name = name
        self.opis = opis
        self.dedline = dedline
        self.stan = False
class Taskmgr:
    def __init__(self):
        self.taskList=[]

    def add_task(self,task):
        self.taskList.append(task)

    def remove_task(self,index):
        if 0 <= index <=