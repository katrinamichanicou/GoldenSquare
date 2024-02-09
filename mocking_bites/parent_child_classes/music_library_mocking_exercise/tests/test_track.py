from lib.track import Track

def test_title_is_string():
    track_1 = Track("Just", "Amtrac")
    assert type(track_1.title) == str

def test_artist_is_string():
    track_1 = Track("Just", "Amtrac")
    assert type(track_1.artist) == str

def test_keyword_returns_true_if_in_title():
    track_1 = Track("Every Cow Has A Bird", "Guti & Dubshape")
    assert track_1.matches("Cow") == True

def test_keyword_returns_true_if_in_artist():
    track_1 = Track("Every Cow Has A Bird", "Guti & Dubshape")
    assert track_1.matches("Guti") == True

def test_keyword_returns_false_if_not_in_title():
    track_1 = Track("Every Cow Has A Bird", "Guti & Dubshape")
    assert track_1.matches("Hello") == False

def test_keyword_returns_false_if_not_in_artist():
    track_1 = Track("Every Cow Has A Bird", "Guti & Dubshape")
    assert track_1.matches("Hello") == False
