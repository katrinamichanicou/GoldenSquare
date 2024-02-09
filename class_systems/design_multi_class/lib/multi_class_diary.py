# Potential Improvements:
#   1. Update diary entries to dictionary with date, contents, contacts, tasks_todo_today as keys
#   2. Split out classes further (six classes instead of three)
#      1.PhoneNumbers --> 2.Diary
#      3.DiaryEntry --> 2.Diary
#      4.ReadableEntry --> 2.Diary
#      5.Task --> 6.TaskList




class Diary():

    def __init__(self):
        self.diary_entries = []
        self.tasks = []
        self.contacts = []

    def add_diary_entry(self, diary_entry):
        self.diary_entries.append(diary_entry)

    def search_entries(self, date_keyword = ""):
        if date_keyword == "":
            return self.diary_entries
        
        search_results = []
        for entry in self.diary_entries:
            if date_keyword in entry.date or date_keyword in entry.contents:
                search_results.append(entry)
        return search_results

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

    def add_task(self, task):
        self.tasks.append(task)

    def list_incomplete_tasks(self):
        return [task for task in self.tasks if task.completed == False]

    def list_phone_numbers(self):
        return [entry.contact_details for entry in self.diary_entries if entry.contact_details != None]

