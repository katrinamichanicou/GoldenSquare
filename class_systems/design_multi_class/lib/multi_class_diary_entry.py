import re

class DiaryEntry:

    def __init__(self, date, contents):
        
        if bool(re.match(r'^\d{2}/\d{2}/\d{4}$', date)) == False:
            raise Exception("Date is in incorrect format, please enter as dd/mm/yyyy")
        
        self.date = date
        self.contents = contents
        self.contents_list = list(self.contents.split())
        
        
        if ": +" in self.contents:
            for word in self.contents_list:
                if ":" in word:
                    contact_name = word[:-1]
        
            phone_number = self.contents[self.contents.index(": +")+2:self.contents.index(": +")+15]
            self.contact_details = {contact_name : phone_number}

    
    def count_words(self):
        return len(self.contents_list)


    # BELOW LINES REFACTORED ON LINES 15-21 above
    # def contact(self):
    #     if ": +" not in self.contents:
    #         raise Exception("No contact found in diary entry contents.")
    #     else:
    #         for word in self.contents_list:
    #             if ":" in word:
    #                 contact_name = word[:-1]
        
    #         phone_number = self.contents[self.contents.index(": +")+2:self.contents.index(": +")+15]
    #         self.contact_details = {contact_name : phone_number}

    #     return self.contact_details
