from lib.multi_class_todo import *
import pytest

"""
Given a todo instance
Return the task property
"""
def test_task_property():
    task_1 = Todo("Complete Chapter 1", "19/01/2024")
    assert task_1.task == "Complete Chapter 1"

"""
Given a todo instance
Return the complete by date property=
"""
def test_complete_by_property():
    task_1 = Todo("Complete Chapter 1", "19/01/2024")
    assert task_1.complete_by == "19/01/2024"

"""
Given a todo instance
Check that complete_by is in the correct date format
"""
def test_complete_by_date_format():
    with pytest.raises(Exception) as e:
        task_1 = Todo("Complete Chapter 1", "19/01/24")
    assert str(e.value) == "Date is in incorrect format, please enter as dd/mm/yyyy"

"""
Given a todo instance
Return the default (initial) status of the task completed property as False
"""
def test_initial_status_false():
    task_1 = Todo("Complete Chapter 1", "19/01/2024")
    assert task_1.completed == False

"""
Given a todo instance
When the mark complete task is called
Return the task completed property to confirm it has updated to True
"""
def test_returns_true_when_marked_as_complete():
    task_1 = Todo("Complete Chapter 1", "19/01/2024")
    task_1.mark_complete()
    assert task_1.completed == True