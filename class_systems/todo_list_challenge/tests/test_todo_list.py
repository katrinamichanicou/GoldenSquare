from lib.todo_list import TodoList
import pytest

"""
Initially returns empty list
"""
def test_todo_list_empty():
    todo_list = TodoList()
    assert todo_list.todo_list == []

#  Code refactored - test no longer required
# """
# Initially status dictionary is empty
# """
# def test_todo_status_empty():
#     todolist = TodoList()
#     assert todolist.todo_status == {}

"""
For incomplete method raise exception if there are no tasks in the list
"""
def test_no_tasks_raises_error_for_incomplete():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.incomplete()
    assert str(e.value) == "No tasks in list!"

"""
For complete method raise exception if there are no tasks in the list
"""
def test_no_tasks_raises_error_for_complete():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.complete()
    assert str(e.value) == "No tasks in list!"

"""
For give up method raise exception if there are no tasks in the list
"""
def test_no_tasks_raises_error_for_give_up():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.give_up()
    assert str(e.value) == "No tasks in list!"