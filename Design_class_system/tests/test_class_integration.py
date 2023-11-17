
from lib.Diary_book import *
from lib.Contacts import *
from lib.diary_entry import DiaryEntry
from lib.to_do import *
'''
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


Classes that will be needed:
    *DiaryBook - will store diary entries and todo tasks and contacts.
    *Diary_entry - To create individual diary entries that can be fed into DiaryBook. It will also need to work out their reading time.
    *Contacts - To create individual contact cards
    *ToDoList - Stores tasks to be done and completed tasks.
'''

'''
Integration tests.
'''

'''
Integration with DiaryEntry.
'''

'''
I want to be able to add a diary entry to DiaryBook then access that entry.
'''

diary_entry1 = DiaryEntry('Test Title','This is some test contents.')
diary_entry2 = DiaryEntry('Test Title','This is some longer test contents2.')
diary_entry3 = DiaryEntry('Test Title','This shorter test contents3.')
diary_entry4 = DiaryEntry('Test Title','Test ' *200)
diary_entry5 = DiaryEntry('Test Title','Test ' *501)
diary_entry6 = DiaryEntry('Test Title','Test ' *1000)
to_do_list1 = ToDo()
to_do_list1.add_task('Task1')
to_do_list1.add_task('Task2')
to_do_list1.add_task('Task3')
to_do_list1.add_task('Task4')
to_do_list1.remove_completed_tasks('Task4') #self.todo_list == ['Task1','Task2','Task3'] self.completed_list == ['Task4']
contact1 = Contacts('Terry','08001234567')
contact2 = Contacts('Jerry','08007654321')
contact3 = Contacts('Larry','08007456123')
diary_entry1.add_contact(contact1)
diary_entry2.add_contact(contact2)
diary_entry3.add_contact(contact3)

def test_add_diary_entry_to_DiaryBook():
    test_diary = DiaryBook()
    diary_entry1 = DiaryEntry('Test Title','This is some test contents.')
    test_diary.add_diary_entry(diary_entry1)
    assert test_diary.get_diary_entry(1) == 'Test Title: This is some test contents.'

'''
I want to be able to list all my diary entries so that they can be read.
'''
def test_list_all_diary_entries_from_DiaryBook():
    test_diary = DiaryBook()
    test_diary.add_diary_entry(diary_entry1)
    test_diary.add_diary_entry(diary_entry2)
    test_diary.add_diary_entry(diary_entry3)
    assert test_diary.get_all_diary_entries() == [diary_entry1,diary_entry2,diary_entry3]

'''
I want to be able to list the available diary entries that I can read based on how
much time i have and my reading speed.
'''

def test_reading_time_returns_viable_diary_entries():
    test_diary = DiaryBook()
    test_diary.add_diary_entry(diary_entry4)
    test_diary.add_diary_entry(diary_entry5)
    test_diary.add_diary_entry(diary_entry6)
    assert test_diary.entries_to_read(200,3) == [diary_entry4,diary_entry5]


'''
I want to add a todo list to my diary. Then I want to be able to see the tasks that
I have left and those that I have completed.
'''

def test_add_todo_list_see_todos():
    test_diary = DiaryBook()
    test_diary.add_todo_list(to_do_list1)
    assert test_diary.todo_list.show_todo_list() == ['Task1','Task2','Task3']

def test_add_todo_list_see_completed():
    test_diary = DiaryBook()
    test_diary.add_todo_list(to_do_list1)
    assert test_diary.todo_list.show_completed_list() == ['Task4']

'''
I want to be able to add a contact to my diary entry to keep track of my names and
phone numbers
'''

def test_add_contact_to_diary_entry():
    diary_entry1.add_contact(contact1)
    assert diary_entry1.display_contact() == contact1

'''
I want to be able to list all of my contacts from all my entries. If there is no contact
it should return an empty list.
'''

def test_all_contacts_returns_contacts():
    test_diary = DiaryBook()
    test_diary.add_diary_entry(diary_entry1)
    test_diary.add_diary_entry(diary_entry2)
    test_diary.add_diary_entry(diary_entry3)
    test_diary.add_diary_entry(diary_entry4)
    test_diary.add_diary_entry(diary_entry5)
    test_diary.add_diary_entry(diary_entry6)
    assert test_diary.get_all_contacts() == [contact1,contact2,contact3]

'''
I want to be able to see if an entry has a contact. Return the contact if true or a
message that states no contact information exists.
'''

def test_get_contact_for_entry():
    test_diary = DiaryBook()
    test_diary.add_diary_entry(diary_entry1)
    test_diary.add_diary_entry(diary_entry2)
    test_diary.add_diary_entry(diary_entry3)
    test_diary.add_diary_entry(diary_entry4)
    test_diary.add_diary_entry(diary_entry5)
    test_diary.add_diary_entry(diary_entry6)
    assert test_diary.get_contact(1) == contact1
    assert test_diary.get_contact(4) == 'There is no contact information.'


