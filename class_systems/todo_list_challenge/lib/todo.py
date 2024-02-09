# File: lib/todo.py
class Todo:

    def __init__(self, task):
        if task == "":
            raise Exception("Cannot enter empty string for task!")
        self.task = task
        self.completed = False
        

    def mark_complete(self):
        self.completed = True
        


todo = Todo("")
print(todo.task)