import re

class Todo:
    # User-facing properties:
    #   task: string
    #   complete_by: string in the format 'dd/mm/yyyy'

    def __init__(self, task, complete_by):
        if bool(re.match(r'^\d{2}/\d{2}/\d{4}$', complete_by)) == False:
            raise Exception("Date is in incorrect format, please enter as dd/mm/yyyy")
        self.complete_by = complete_by
        self.task = task
        self.completed = False

    def mark_complete(self):
        self.completed = True
