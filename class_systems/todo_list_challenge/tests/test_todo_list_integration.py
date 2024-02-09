from lib.todo_list import TodoList
from lib.todo import Todo

"""
test that add method adds instance of each task to the todo_list
"""
def test_todo_added_to_list():
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    todolist = TodoList()
    todolist.add(task_1)
    todolist.add(task_2)
    assert todolist.todo_list == [task_1, task_2]

#  Code refactored - test no longer required
# """
# test that add method adds the status of each task to the todo_status dictionary
# note: the status for all tasks should be False initially
# """
# def test_todo_status_added():
#     task_1 = Todo("Task 1")
#     task_2 = Todo("Task 2")
#     todolist = TodoList()
#     todolist.add(task_1)
#     todolist.add(task_2)
#     assert todolist.todo_status == {task_1 : False, task_2 : False}


"""
test that incomplete method returns a list of incomplete tasks
this should be all tasks where the complete status is False
"""
def test_incomplete_task_list():
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    todolist = TodoList()
    todolist.add(task_1)
    todolist.add(task_2)
    assert todolist.incomplete() == [task_1, task_2]

"""
test that if test is marked as complete it is then removed from the incomplete tasks list
"""
def test_updated_incomplete_tasks():
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    todolist = TodoList()
    todolist.add(task_1)
    todolist.add(task_2)
    task_1.mark_complete()
    assert todolist.incomplete() == [task_2]

"""
Test that complete tasks list initially empty
"""
def test_complete_tasks_empty():
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    todolist = TodoList()
    todolist.add(task_1)
    todolist.add(task_2)
    assert todolist.complete() == []


"""
test that all completed (True) tasks are returned when complete method is run
"""
def test_completed_task_list():
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    todolist = TodoList()
    todolist.add(task_1)
    todolist.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert todolist.complete() == [task_1, task_2]

"""
Test that give_up method updates all tasks from False to True
"""
def test_give_up_updates_to_true():
    task_1 = Todo("Task 1")
    task_2 = Todo("Task 2")
    todolist = TodoList()
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.give_up()
    assert todolist.complete() == [task_1, task_2]



