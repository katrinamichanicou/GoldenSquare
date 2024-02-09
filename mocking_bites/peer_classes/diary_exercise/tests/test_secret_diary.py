from lib.secret_diary import SecretDiary
from unittest.mock import Mock
import pytest

def test_diary_locked_initially():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"
    # can also add in an assert to confirm that the diary.read() function has not been called
    # when the secret_diary.read() function has been called and the diary is locked
    # see below
    fake_diary.read.assert_not_called

def test_unlocked_diary_returns_contents():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    fake_diary.read.return_value = "This is interesting."
    secret_diary.unlock()
    assert secret_diary.read() == "This is interesting."

def test_diary_unlocked_and_locked_again_raises_exception():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"