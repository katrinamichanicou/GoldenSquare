# File: lib/music_library.py

class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def search(self, keyword):
        return [track for track in self.tracks if track.matches(keyword)]