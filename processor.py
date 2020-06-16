from dataclasses import dataclass
from task import Task

@dataclass()
class Thread:
    time_work: int = None
    task_type: int = None
    idle: bool = True

class Processor():
    def __init__(self): 
        self.p = Thread()
        
    def add_task(self, task: Task):
        if self.p.task_type < task.get_type():
            l = Task()
            l.set_type(task.get_type())
            l.set_time(task.get_time())
            stack.add_item(l)
            self.p.time_work = task.get_time()
            self.p.task_type = task.get_type()
        elif self.idle_proc():
            self.p.time_work = task.get_time()
            self.p.task_type = task.get_type()
        else:
            stack.add_item(task)

    def __task_perform_p(self):
        self.p.time_work -= 1
        if self.p.time_work <= 0:
            self.p.idle = True
            self.p_task_type = None

    def __str__(self):
        string = "|proc|type|time|idle|"
        if not self.p.idle:
            string += "\n|1   |{:<4}|{:<4}|{:<4}|".format(str(self.p.task_type), str(self.p.time_work), str(self.p.idle))
        else:
            string += "\n|1   |None|None|True|"
        return string

    def work(self):
        if not self.p.idle:
            self.__task_perform_p()
        else:
            self.p.idle = True

    def idle_proc(self):
        return self.p.idle