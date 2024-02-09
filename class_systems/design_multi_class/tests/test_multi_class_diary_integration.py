from lib.multi_class_diary import *
from lib.multi_class_diary_entry import *
from lib.multi_class_todo import *

"""
Given a diary
When we add two diary entries
We see those entries reflected in the diary list
"""
def test_add_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy.")
    entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    assert diary.diary_entries == [entry_1, entry_2]

"""
Given a diary with two entries
When we search by date
The correct entry is returned
"""
def test_search_entries_by_date():
    diary = Diary()
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy.")
    entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    assert diary.search_entries("15/01/2024") == [entry_1]

"""
Given a diary with two entries
When we search by a keyword that is within the contents of both entries
Both entries are returned as a list
"""
def test_search_entries_by_keyword():
    diary = Diary()
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy.")
    entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    assert diary.search_entries("Today") == [entry_1, entry_2]

"""
Given a diary with two entries
When we search by a keyword that is within the contents of one of the entries
Only that entry is returned
"""
def test_search_entries_by_keyword_in_one_entry():
    diary = Diary()
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy.")
    entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    assert diary.search_entries("Makers") == [entry_1]

"""
Given a diary with two entries
When no date or keyword is given all entries are returned
"""
def test_search_entries_no_arg_returns_full_list():
    diary = Diary()
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy.")
    entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    assert diary.search_entries() == [entry_1, entry_2]

"""
Given a diary with two entries
When we ask to return the best entry with wpm of 5 and number of minutes available of 1
It returns the entry closest matching the length of which can be fully read in that time (eg. entry of 5 words or less)
"""
def test_best_entry_for_5_words():
    diary = Diary()
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy. It was exciting!")
    entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    assert diary.find_best_entry_for_reading_time(5, 1) == entry_2

"""
Given a diary with two entries
When we ask to return the best entry with wpm of 200 and number of minutes available of 10
It returns the entry closest matching the length of which can be fully read in that time (eg. entry of 2,000 words or less)
"""
def test_best_entry_for_2000_words():
    diary = Diary()
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy. It was exciting!")
    entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    assert diary.find_best_entry_for_reading_time(200, 10) == entry_1

"""
Given a diary with two incomplete tasks
When asked to return the list of incomplete takss
It returns a list of both tasks
"""
def test_returns_list_all_incomplete_tasks():
    diary = Diary()
    task_1 = Todo("Complete Chapter 1", "19/01/2024")
    task_2 = Todo("Complete Chapter 2", "26/01/2024") 
    diary.add_task(task_1)
    diary.add_task(task_2)
    assert diary.list_incomplete_tasks() == [task_1, task_2]

"""
Given a diary with two incomplete tasks
Mark one as complete, then when asked to return the list of incomplete takss
It returns a list of the incomplete task only
"""
def test_incomplete_task_list():
    diary = Diary()
    task_1 = Todo("Complete Chapter 1", "19/01/2024")
    task_2 = Todo("Complete Chapter 2", "26/01/2024") 
    diary.add_task(task_1)
    diary.add_task(task_2)
    task_1.mark_complete()
    assert diary.list_incomplete_tasks() == [task_2]

"""
Given a diary with entries containing phone numbers
When asked to return phone numbers
Return a list of dictionaries with the contact as key and phone number as the value
"""
def test_list_phone_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy and met (Paul: +447792773792).")
    entry_2 = DiaryEntry("16/01/2024", "Today I did some coding and met another friend. Helen: +447729828812")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    # entry_1.contact()
    # entry_2.contact()
    assert diary.list_phone_numbers() == [entry_1.contact_details, entry_2.contact_details]