# File: lib/secret_diary.py

class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = True

    def read(self):
        if self.locked == True:
            raise Exception("Go away!")
        return self.diary.read()
        
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
