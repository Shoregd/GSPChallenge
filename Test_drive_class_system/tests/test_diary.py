
from lib.diary import Diary
from lib.diary_entry import *

'''
Diary will be holding instances of Diary_entry.

    *It will need to hold a list of the instances of diary entry.
    *It will need to be able to add a new entry and append it to the list already stored.
    *it will need to display the full list of entries.
    *It will need to count the words in all of the current diary entries that have been added summing
    using the funtion built into diary_entry then return that integer.
    *It will need sum the reading time of all entries then return that value as a integer.
    *It will need to calculate the largest entry that the user can actually read in full 
    and return the instance.
'''

'''
Test that diary initialises with the instance of diary_entry.
'''

def test_init_with_blank_diary_entry():
    test_class = Diary()
    assert test_class.diary_entries == []

'''
Test that add function updates the diary_entries with the diary entry.
'''

def test_add_updates_list_with_instance():
    test_class = Diary()
    diary_entry1 = DiaryEntry('Test Title','This is some test contents.')
    test_class.add(diary_entry1)
    assert test_class.diary_entries == [diary_entry1]

def test_add_updates_list_with_instances():
    test_class = Diary()
    diary_entry1 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry2 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry3 = DiaryEntry('Test Title','This is some test contents.')
    test_class.add(diary_entry1)
    test_class.add(diary_entry2)
    test_class.add(diary_entry3)
    assert test_class.diary_entries == [diary_entry1,diary_entry2,diary_entry3]

'''
Test all funtion returns list of all added entries
'''

def test_all_returns_a_list():
    test_class = Diary()
    
    assert type(test_class.all()) == list

def test_all_returns_all_entries():
    test_class = Diary()
    diary_entry1 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry2 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry3 = DiaryEntry('Test Title','This is some test contents.')
    test_class.add(diary_entry1)
    test_class.add(diary_entry2)
    test_class.add(diary_entry3)
    assert test_class.all() == [diary_entry1,diary_entry2,diary_entry3]

'''
Test that count words returns an integer of the total number of words in all added entries.
'''

def test_count_words_returns_an_integer():
    test_class = Diary()
    diary_entry1 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry2 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry3 = DiaryEntry('Test Title','This is some test contents.')
    test_class.add(diary_entry1)
    test_class.add(diary_entry2)
    test_class.add(diary_entry3)
    assert type(test_class.count_words()) == int

def test_count_words_returns_total_count():
    test_class = Diary()
    diary_entry1 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry2 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry3 = DiaryEntry('Test Title','This is some test contents.')
    test_class.add(diary_entry1)
    test_class.add(diary_entry2)
    test_class.add(diary_entry3)
    assert test_class.count_words() == 21

'''
Test that reading_time returns an integer of the total minutes to read all entries given a set wpm.
'''

def test_reading_time_returns_an_integer():
    test_class = Diary()
    diary_entry1 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry2 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry3 = DiaryEntry('Test Title','This is some test contents.')
    test_class.add(diary_entry1)
    test_class.add(diary_entry2)
    test_class.add(diary_entry3)
    assert type(test_class.reading_time(3)) == int

def test_reading_time_returns_correct_time():
    test_class = Diary()
    diary_entry1 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry2 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry3 = DiaryEntry('Test Title','This is some test contents.')
    test_class.add(diary_entry1)
    test_class.add(diary_entry2)
    test_class.add(diary_entry3)
    assert test_class.reading_time(3) == 7

'''
Test that best reading time returns an instance of diary_entry
'''

def test_best_reading_time_returns_instance():
    test_class = Diary()
    diary_entry1 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry2 = DiaryEntry('Test Title','This is some longer test contents.')
    diary_entry3 = DiaryEntry('Test Title','This shorter test contents.')
    test_class.add(diary_entry1)
    test_class.add(diary_entry2)
    test_class.add(diary_entry3)
    assert test_class.find_best_entry_for_reading_time(10,2) in [diary_entry2,diary_entry1,diary_entry3]

def test_best_reading_time_returns_correct_instance():
    test_class = Diary()
    diary_entry1 = DiaryEntry('Test Title','This is some test contents.')
    diary_entry2 = DiaryEntry('Test Title','This is some longer test contents.')
    diary_entry3 = DiaryEntry('Test Title','This shorter test contents.')
    test_class.add(diary_entry1)
    test_class.add(diary_entry2)
    test_class.add(diary_entry3)
    assert test_class.find_best_entry_for_reading_time(1,7) == diary_entry1
    assert test_class.find_best_entry_for_reading_time(1,8) == diary_entry2
    assert test_class.find_best_entry_for_reading_time(1,6) == diary_entry3

