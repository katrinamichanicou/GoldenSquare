from lib.multi_class_diary_entry import *
import pytest

"""
Given a diary entry with a date and contents
Return the date property
"""
def test_diary_entry_date_property():
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy")
    assert entry_1.date == "15/01/2024"

"""
Given a diary entry instance
Check that date is in the correct format
"""
def test_diary_entry_date_format():
    with pytest.raises(Exception) as e:
        entry_1 = DiaryEntry("15/01/24", "Today I started Makers Academy")
    assert str(e.value) == "Date is in incorrect format, please enter as dd/mm/yyyy"

"""
Given a diary entry with a date and contents
Return the contents property
"""
def test_diary_entry_contents_property():
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy")
    assert entry_1.contents == "Today I started Makers Academy"

"""
Given a diary entry instance
Return the number of words in the contents
"""
def test_diary_entry_length():
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy")
    assert entry_1.count_words() == 5

"""
Given a diary entry with a contact and phone number in the contents
Return the contact name and number as a dictionary
"""
def test_returns_contact_details():
    entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy and met Paul: +447792773792.")
    assert entry_1.contact_details == {"Paul": "+447792773792"}

# """ 
# Given a diary entry without a contact and phone number
# When contact method run it raises an exception
# """
# def test_if_no_contact_raise_exception():
#     entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy")
#     with pytest.raises(Exception) as e:
#         entry_1.contact()
#     assert str(e.value) == "No contact found in diary entry contents."


