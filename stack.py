from  dataclasses import dataclass

@dataclass()
class TaskStack:
    task_list = []
    is_empty = True
    length = 0

class Stack:
    def __init__(self):
        self.stack = TaskStack

    def add_item(self, task):
        self.stack.task_list.append(task)
        self.stack.length += 1
        self.stack.is_empty = False

    def del_item(self):
        if self.stack.length != 0:
            self.stack.length -= 1
            if self.stack.length == 0:
                self.stack.is_empty = True
            return self.stack.task_list.pop(len(self.stack.task_list)-1)
        return -1

    def check_is_empty(self):
        return self.stack.is_empty

    def get_length(self):
        return self.stack.length

    def __str__(self):
        strok = "|type|time|"
        if not self.stack.is_empty:
            for task in self.stack.task_list:
                strok += "\n|{:<4}|{:<4}|".format(str(task.get_type()), str(task.get_time()))
        else:
            strok += "\n|None|None|"
        strok += "\n|____|____|\n\n"
        return strok