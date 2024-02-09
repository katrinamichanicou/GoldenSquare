# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.track = title + " " + artist

    def matches(self, keyword):
        return keyword in self.track