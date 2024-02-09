# Version 3: Import Unittest
# In order to more easily create fake classes / objects
# we can import a new tool from the *unittest* library
from unittest.mock import Mock

from lib.diary import Diary
import pytest

@pytest.mark.skip(reason="not yet implemented")
def test_diary_counts_words_in_all_entries_with_mocks():
    diary = Diary()

    fake_two_word_diary_entry = Mock()
    fake_two_word_diary_entry.count_words.return_value = 2

    fake_three_word_diary_entry = Mock()
    fake_three_word_diary_entry.count_words.return_value = 3

    diary.add(fake_two_word_diary_entry)
    diary.add(fake_three_word_diary_entry)

    assert diary.count_words() == 5


# Version 2: Fake Classes
# Testing using fake classes thereby no longer requiring the DiaryEntry class
# 
# def test_diary_counts_words_in_all_entries_with_fakes():
#     diary = Diary()
#     diary.add(FakeTwoWordDiaryEntry())
#     diary.add(FakeThreeWordDiaryEntry())
#     assert diary.count_words() == 5
#
#
# class FakeTwoWordDiaryEntry:
#     def count_words(self):
#         return 2
#
#
# class FakeThreeWordDiaryEntry:
#     def count_words(self):
#         return 3

# ----------------------------------------------------------------------------

# Version 1: Integration
# Testing using class integration (multiple classes)
# from lib.diary_entry import DiaryEntry
#
# def test_diary_counts_words_in_all_entries():
#     diary = Diary()
#     diary.add(DiaryEntry("title1", "one two"))
#     diary.add(DiaryEntry("title2", "three four five"))
#     assert diary.count_words() == 5

