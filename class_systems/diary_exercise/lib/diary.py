import math
import sys
print(sys.path)

class Diary:
    def __init__(self):
        self.diary_entries = []

    def add(self, entry):
        self.diary_entries.append(entry)

    def all(self):
        return self.diary_entries

    def count_total_words(self):
        total_words = 0
        for entry in self.diary_entries:
            total_words += entry.count_words()
        return total_words

    def reading_time(self, wpm):
        return math.ceil(self.count_total_words() / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        number_words_read = wpm * minutes
        best_entry = None
        longest_so_far = 0
        for entry in self.diary_entries:
            words = entry.count_words()
            if words <= number_words_read and words > longest_so_far:
                best_entry = entry
                longest_so_far = words
        return best_entry
            #best_entry_tracker[entry] = (number_words_read - self.count_words())
        

        #return sorted(best_entry_tracker) 

        
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        

