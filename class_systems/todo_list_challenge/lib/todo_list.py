# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.todo_list = []


    def add(self, todo):
        self.todo_list.append(todo)

    def incomplete(self):
        if self.todo_list == []:
            raise Exception("No tasks in list!")
        return [task for task in self.todo_list if task.completed == False]
        # incomplete_tasks = []
        # for task in self.todo_list:
        #     if task.completed == False:
        #         incomplete_tasks.append(task)
        #return incomplete_tasks

    def complete(self):
        if self.todo_list == []:
            raise Exception("No tasks in list!")
        return [task for task in self.todo_list if task.completed == True]

    def give_up(self):
        if self.todo_list == []:
            raise Exception("No tasks in list!")
        for task in self.todo_list:
            task.mark_complete()


