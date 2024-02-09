# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│    Diary                                                │
│                                                         │
│    - diary entry                                        │
│                                                         │
│    - add (diary entry)                                  │
│                                                         │
│    - search_by_entry(date or keyword (opt. arguments?)  │
│      ==> [entries]                                      │
│                                                         │
│    - find_best_entry_for_reading_time (wpm,time)        │
│      ==> entry                                          │
│                                                         │
│    - list_incomplete_tasks() ==> [incomplete tasks]     │
│                                                         │
│    - list_phone_numbers ==> [{contact : num}, {.:.}]    │
│                                                         │
│                                                         │
└────────────────┬───────────────────────────┬────────────┘
                 │                           │
                 │                           │
                 │                           │
                 ▼                           ▼
 ┌────────────────────────────┬───────────────────────────┬
 │                            │                           │                           
 │    DiaryEntry              │  Todo                     │                           
 │                            │                           │                           
 │    - date                  │  - task                   │                           
 │    - content               │  - complete by date       │                           
 │                            │                           │                           
 │    - find_phone_number_    │  - mark_complete()        │                           
 │      and_contact()         │                           │                           
 │      ==> {contact : num}   │                           │                           
 │                            │                           │
 └────────────────────────────┴───────────────────────────┴


```

_Also design the interface of each class in more detail._

```python
class Diary:
    # User-facing properties:
    #   diary entries: list of diary entries
    #   tasks: todo list of tasks

    def __init__(self):
        pass # No code here yet

    def add_diary_entry(self, diary_entry):
        # Parameters:
        #   DiaryEntry: an instance of a diary entry
        # Side-effects:
        #   Adds the track to the tracks property of the self object
        pass # No code here yet

    def search_entries(self, date(optional), keyword(optional)):
        # Parameters:
        #   date(optional): string
        #   keyword(optional): string
        # Returns:
        #   A list of the DiaryEntry objects for the date specified OR have contents that include the keyword
        pass # No code here yet

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm: integer representing average words the user can read per minute
        #   minutes: integer representing number of minutes user has available
        # Returns:
        #   The diary entry of a length that best fits based on the users wpm and mintues available
        pass # No code here yet

    def add_todo(self, todo):
        # Parameters:
        #   Todo: an instance of a task todo
        # Side-effects:
        #   Adds the task to the list of tasks todo
        pass # No code here yet

    def list_incomplete_tasks(self):
        # Returns:
        #   List of incomplete tasks
        pass # No code here yet

    def list_phone_numbers(self):
        # Returns:
        #   List of dictionaries containing contact names and their phone numbers
        pass # No code here yet


class DiaryEntry:
    # User-facing properties:
    #   date: string in the format 'dd/mm/yyyy'
    #   contents: string 

    def __init__(self, date, contents):
        # Parameters:
        #   date: string in the format 'dd/mm/yyyy'
        #   contents: string   
        pass # No code here yet

    def contact(self):
        # Returns:
        #   A dictionary in the form of {contact_name : phone_number}
        pass # No code here yet


class Todo:
    # User-facing properties:
    #   task: string
    #   complete_by: string in the format 'dd/mm/yyyy'

    def __init__(self, task, complete_by):
        # Parameters:
        #   task: string
        #   complete_by: string in the format 'dd/mm/yyyy'
        #   property(task) completed = False
        pass # No code here yet

    def mark_complete(self):
        # Side-effects:
        #   marks task as complete
        #   sets task property of completed to True
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a diary
When we add two diary entries
We see those entries reflected in the diary list
"""
diary = Diary()
entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy.")
entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
diary.add_diary_entries(entry_1)
diary.add_diary_entries(entry_2)
diary.entries == [entry_1, entry_2]

"""
Given a diary with two entries
When we search by date
The correct entry is returned
"""
diary = Diary()
entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy.")
entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
diary.add_diary_entries(entry_1)
diary.add_diary_entries(entry_2)
diary.search_entries("15/01/2024") == [entry_1]

"""
Given a diary with two entries
When we search by a keyword that is within the contents of both entries
Both entries are returned as a list
"""
diary = Diary()
entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy.")
entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
diary.add_diary_entries(entry_1)
diary.add_diary_entries(entry_2)
diary.search_entries("Today") == [entry_1, entry_2]

"""
Given a diary with two entries
When we search by a keyword that is within the contents of one of the entries
Only that entry is returned
"""
diary = Diary()
entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy.")
entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
diary.add_diary_entries(entry_1)
diary.add_diary_entries(entry_2)
diary.search_entries("Makers") == [entry_1, entry_2]


"""
Given a diary with two entries
When we ask to return the best entry with wpm of 5 and number of minutes available of 1
It returns the entry closest matching the length of which can be fully read in that time (eg. entry of 5 words or less)
"""
diary = Diary()
entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy.")
entry_2 = DiaryEntry("16/01/2024", "Today I did some coding")
diary.add_diary_entries(entry_1)
diary.add_diary_entries(entry_2)
diary.find_best_entry_for_reading_time(5, 1) == entry_2

"""
Given a diary with two incomplete tasks
When asked to return the list of incomplete takss
It returns a list of both tasks
"""
diary = Diary()
task_1 = Todo("Complete Chapter 1", "19/01/2024")
task_2 = Todo("Complete Chapter 2", "26/01/2024") 
diary.add_todo(task_1)
diary.add_todo(task_2)
diary.list_incomplete_tasks() == [todo_1, todo_2]

"""
Given a diary with two incomplete tasks
Mark one as complete, then when asked to return the list of incomplete takss
It returns a list of the incomplete task only
"""
diary = Diary()
task_1 = Todo("Complete Chapter 1", "19/01/2024")
task_2 = Todo("Complete Chapter 2", "26/01/2024") 
diary.add_todo(task_1)
diary.add_todo(task_2)
task_1.mark_complete()
diary.list_incomplete_tasks() == [todo_2]

"""
Given a diary with entries containing phone numbers
When asked to return phone numbers
Return a list of dictionaries with the contact as key and phone number as the value
"""
diary = Diary()
entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy and met Paul M(num:07792773792).")
entry_2 = DiaryEntry("16/01/2024", "Today I did some coding and met another friend. Helen F num: 07729828812")
diary.add_diary_entries(entry_1)
diary.add_diary_entries(entry_2)
diary.list_phone_numbers() == [entry_1.contact, entry_2.contact]

```



## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

DiaryEntry
"""
Given a diary entry with a date and contents
Return the date property
"""
entry_1 = Diary_Entry("15/01/2024", "Today I started Makers Academy")
entry_1.date == "15/01/2024"

"""
Given a diary entry with a date and contents
Return the contents property
"""
entry_1 = Diary_Entry("15/01/2024", "Today I started Makers Academy")
entry_1.contents == "Today I started Makers Academy"

"""
Given a diary entry with a contact and phone number in the contents
Return the contact name and number as a dictionary
"""
entry_1 = DiaryEntry("15/01/2024", "Today I started Makers Academy and met Paul M(num:07792773792).")
entry_1.contact() == {"Paul M", "07792773792"}

Todo
"""
Given a todo instance
Return the task property
"""
task_1 = Todo("Complete Chapter 1", "19/01/2024")
task_1.task == "Complete Chapter 1"

"""
Given a todo instance
Return the complete by date property=
"""
task_1 = Todo("Complete Chapter 1", "19/01/2024")
task_1.complete_by == "19/01/2024"

"""
Given a todo instance
Return the default (initial) status of the task completed property as False
"""
task_1 = Todo("Complete Chapter 1", "19/01/2024")
task_1.completed == False

"""
Given a todo instance
When the mark complete task is called
Return the task completed property to confirm it has updated to True
"""
task_1 = Todo("Complete Chapter 1", "19/01/2024")
task_1.mark_complete()
task_1.completed == True


```


_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
