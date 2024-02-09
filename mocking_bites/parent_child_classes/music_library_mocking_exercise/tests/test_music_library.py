from lib.music_library import MusicLibrary
from lib.track import Track
from unittest.mock import Mock

"""
Integration Test
When I add multiple tracks
They are reflected in the tracks list
"""
def test_tracks_added_to_list_integration_version():
    music_library = MusicLibrary()
    track_1 = Track("Just", "Amtrac")
    track_2 = Track("Every Cow Has A Bird", "Guti & Dubshape")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.tracks == [track_1, track_2]

"""
Mock Test
When I add multiple tracks
They are reflected in the tracks list
"""
def test_tracks_added_to_list_mocking_version():
    music_library = MusicLibrary()
    
    fake_track_1 = Mock()
    fake_track_1.return_value = ("Just", "Amtrac")
    
    fake_track_2 = Mock()
    fake_track_2.return_value = ("Every Cow Has A Bird", "Guti & Dubshape")

    music_library.add(fake_track_1)
    music_library.add(fake_track_2)
    assert music_library.tracks == [fake_track_1, fake_track_2]

"""
Integration Test
When I add multiple tracks
And I search for a track title
Then I get the matching track back
"""
def test_search_returns_track_with_keyword_integration_version():
    music_library = MusicLibrary()
    track_1 = Track("Just", "Amtrac")
    track_2 = Track("Every Cow Has A Bird", "Guti & Dubshape")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search("Just") == [track_1]

def test_search_returns_track_with_keyword_mocking_version():
    music_library = MusicLibrary()

    fake_track_1 = Mock()
    fake_track_1.matches.return_value = True

    music_library.add(fake_track_1)
    music_library.search("Just") == [fake_track_1]

def test_search_returns_correct_track_with_keyword_mocking_version():
    music_library = MusicLibrary()

    fake_track_1 = Mock()
    fake_track_1.matches.return_value = False

    fake_track_2 = Mock()
    fake_track_2.matches.return_value = True

    music_library.add(fake_track_1)
    music_library.add(fake_track_2)

    assert music_library.search("Just") == [fake_track_2]

    def jdskdls():
        bfjsbfjks in dasknldna
        return vkfdnfsk
    
    ften