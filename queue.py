from dataclasses import dataclass
from task import Task


@dataclass()
class QueueData:
    task_type = []
    is_empty: bool = True

class Queue():

    def __init__(self):
        self.q1 = QueueData()
        self.q2 = QueueData()
        self.q3 = QueueData()

    def add_task(self, task:Task):
        if task.get_type() == 0:
            self.q1.task_type.append(task)
            self.q1.is_empty = False
        elif task.get_type() == 1:
            self.q2.task_type.append(task)
            self.q2.is_empty = False
        elif task.get_type() == 2:
            self.q3.task_type.append(task)
            self.q3.is_empty = False

    def del_task(self):
        if not self.q1.is_empty:
            task = self.q1.task_type.pop(0)
            if len(self.q1.task_type) == 0:
                self.q1.is_empty = True
        elif not self.q2.is_empty:
            task = self.q2.task_type.pop(0)
            if len(self.q2.task_type) == 0:
                self.q2.is_empty = True
        elif not self.q3.is_empty:
            task = self.q3.task_type.pop(0)
            if len(self.q3.task_type) == 0:
                self.q3.is_empty = True
        else:
            task = -1
        return task

    def __str__(self):
        return str(str(self.q1.task_type) + str(self.q1.is_empty) + str(self.q2.task_type)  + str(self.q2.is_empty) + str(self.q3.task_type) + str(self.q3.is_empty))

    def get_queue_empty_flag(self):
        return self.q1.is_empty and self.q2.is_empty and self.q3.is_empty