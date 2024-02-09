from lib.todo import Todo
import pytest

"""
Test that the completed property for a task is initially set to False
"""
def test_initially_false():
    task = Todo("Task 1")
    assert task.completed == False

"""
Test that a completed task status is updated to True
"""
def test_mark_complete_updates_status():
    task = Todo("Task 1")
    task.mark_complete()
    assert task.completed == True

"""
Test that initial instance raises error if empty string entered
"""
def test_mark_complete_raises_error():
    with pytest.raises(Exception) as e:
        task = Todo("")
    assert str(e.value) == "Cannot enter empty string for task!"
