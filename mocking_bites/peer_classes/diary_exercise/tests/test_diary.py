from lib.diary import Diary

def test_read_returns_contents():
    diary = Diary("Things in here")
    assert diary.read() == "Things in here"
