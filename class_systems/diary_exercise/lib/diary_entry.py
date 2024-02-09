import math

class DiaryEntry:

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.updated_contents_as_list = self.contents.split()

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        number_words_read = wpm * minutes
        if self.updated_contents_as_list == []:
            self.updated_contents_as_list = self.contents.split()
        chunk = self.updated_contents_as_list[0: number_words_read]
        for word in chunk:
            self.updated_contents_as_list.remove(word)
        return " ".join(chunk)
