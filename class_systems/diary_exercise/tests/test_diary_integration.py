from lib.diary import Diary
from lib.diary_entry import DiaryEntry

# Tests
# Initial thoughts to test DiaryEntry first.
# Copy tests from previous DiaryEntry exercise

# 1. Test that the count_words method returns the number of words in the contents
def test_count_words_returns_num_words():
    diary_entry = DiaryEntry("Thursday 1st February 2024", "Today I debugged some code!")
    result = diary_entry.count_words()
    assert result == 5


# 2. Test that reading_time method returns the reading time (of the 'contents') in minutes
def test_reading_time_returns_correct_minutes():
    diary_entry = DiaryEntry("Thursday 1st February 2024", "Today I debugged some code!")
    result = diary_entry.reading_time(2)
    assert result == 3


# 4. Test reading_chunk calls first chunk of words
# For example if reading time is 4 wpm then and time give is 1 minute
# the result should be the first 4 words
def test_reading_chunk_returns_first_chunk():
    diary_entry = DiaryEntry("Thursday 1st February 2024", "Today I had an espresso, then had some toast and debugged some code. I really enjoyed debugging! I then had a great pairing session with Reeva.")
    result = diary_entry.reading_chunk(4, 1)
    assert result == "Today I had an"

# 5. Test that calling reading_chunk twice returns first chunk and then second
# For example with reading time as 4 wpm and time given = 1 minute
# the result of the second iteration of calling the reading_chunk
# should return the next 4 words
def test_reading_chunk_returns_second_chunk():
    diary_entry = DiaryEntry("Thursday 1st February 2024", "Today I had an espresso, then had some toast and debugged some code. I really enjoyed debugging! I then had a great pairing session with Reeva.")
    diary_entry.reading_chunk(4, 1)
    result = diary_entry.reading_chunk(4, 1)
    assert result == "espresso, then had some"

# 6. Test for second reading chunk with different wpm and minutes
def test_reading_chunk_with_different_times():
    diary_entry = DiaryEntry("Thursday 1st February 2024", "Today I had an espresso, then had some toast and debugged some code. I really enjoyed debugging! I then had a great pairing session with Reeva.")
    diary_entry.reading_chunk(4, 2)
    result = diary_entry.reading_chunk(2, 6)
    assert result == "toast and debugged some code. I really enjoyed debugging! I then had"

# 7. Test that reading_chunk goes back to the start of contents
# Once all contents have been output
def test_that_reading_chunk_starts_again():
    diary_entry = DiaryEntry("Thursday 1st February 2024", "Today I had an espresso, then had some toast and debugged some code. I really enjoyed debugging! I then had a great pairing session with Reeva.")
    print(diary_entry.reading_chunk(26, 1))
    result = diary_entry.reading_chunk(5, 1)
    assert result == "Today I had an espresso,"

# 8. Test that reading_chunk returns correct words
# when wpm and minutes would mean that the person would read beyond the diary entry
def test_that_reading_chunk_returns_full_text():
    diary_entry = DiaryEntry("Thursday 1st February 2024", "Today I had an espresso, then had some toast and debugged some code. I really enjoyed debugging! I then had a great pairing session with Reeva.")
    print(diary_entry.reading_chunk(300, 10))
    result = diary_entry.reading_chunk(5, 1)
    assert result == "Today I had an espresso,"

# Now that the DiaryEntry class has been tested
# I will start test driving the Diary class

# 8. Test that diary entry list is empty initially
def test_initial_status_diary_list():
    diary = Diary()
    assert diary.all() == []

# 9. Test that adding a DiaryEntry instance
# adds a diary entry to the list
# This also tests the Diary method all returns the list
def test_diary_entry_added():
    diary_entry_1 = DiaryEntry("Monday", "Today I had fun.")
    diary = Diary()
    diary.add(diary_entry_1)
    assert diary.all() == [diary_entry_1]

# 10. Test that adding a second DiaryEntry instance
# is added to the list
def test_two_diary_entries_added():
    diary_entry_1 = DiaryEntry("Monday", "Today I had fun.")
    diary_entry_2 = DiaryEntry("Tuesday", "Today I went to the gym.")
    diary = Diary()
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.all() == [diary_entry_1, diary_entry_2]

# 11. Test that count words returns the number of words
# in all diary entries (within list)
# assumption that this relates to the number of words in contents only
def test_count_of_all_entries():
    diary_entry_1 = DiaryEntry("Monday", "Today I had fun.")
    diary_entry_2 = DiaryEntry("Tuesday", "Today I went to the gym.")
    diary = Diary()
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_total_words() == 10

# 12. Test that reading_time returns estimated reading time
# of all entries in diary
# again assumption this relates to contents only
def test_reading_time_of_all_entries():
    diary_entry_1 = DiaryEntry("Monday", "Today I had fun.")
    diary_entry_2 = DiaryEntry("Tuesday", "Today I went to the gym.")
    diary = Diary()
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.reading_time(4) == 3

# 13. Test that the best reading time method
# correctly returns the best diary entry
# for the reading time and speed specified
def test_best_entry_for_reading_time():
    diary_entry_1 = DiaryEntry("Monday", "Today I had fun.")
    diary_entry_2 = DiaryEntry("Tuesday", "Today I went to the gym.")
    diary = Diary()
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.find_best_entry_for_reading_time(4, 1) == diary_entry_1

# 14. Test best reading time method when number of words read
# is more than best entry returns closest entry
def test_best_entry_with_next_best_entry():
    diary_entry_1 = DiaryEntry("Tuesday", "Today I went to the gym.")
    diary_entry_2 = DiaryEntry("Monday", "Today I had fun.")
    diary = Diary()
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.find_best_entry_for_reading_time(5, 1) == diary_entry_2

# 14. Test best reading time method when number of words read
# is more than best entry returns closest entry
def test_best_entry_with_next_best_entry():
    diary_entry_1 = DiaryEntry("Monday", "Today I went to the gym.")
    diary_entry_2 = DiaryEntry("Tuesday", "Today I had fun.")
    diary_entry_3 = DiaryEntry("Wednesday", "Today I ate an orange")
    diary = Diary()
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.find_best_entry_for_reading_time(5, 1) == diary_entry_3

# 15. Test that best entry returns None if no entries are given, ie. list is empty

def test_best_entry_returns_none_if_empty():
    diary = Diary()
    assert diary.find_best_entry_for_reading_time(5, 1) == None