from lib.design_a_class import *
import pytest
'''
Test that the system accepts and assigns the base parameters during __init__
'''

def test_class_init():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert test_class.title == 'Test Title'
    assert test_class.contents == 'This is some test contents.'

'''
Test that the system can return a string when asked to format the data it holds.
'''

def test_format_returns_a_string():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert type(test_class.format()) == str

'''
Test that the system can return the correct data.
'''

def test_correct_data_returned_for_format():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert 'Test Title' in test_class.format()
    assert 'This is some test contents.' in test_class.format()

'''
Test that the system returns the correct data in the correct format as outlined in method statement.
'''

def test_correct_format_for_correct_data():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert test_class.format() == 'Test Title: This is some test contents.'

'''
Test that system can recognise when colon is at end of title and not double up the punctuation.
'''

def test_correct_format_for_title_ending_in_colon():
    test_class = DiaryEntry('Test Title:','This is some test contents.')
    assert test_class.format() == 'Test Title: This is some test contents.'

'''
Test that function "count_words" returns an integer.
'''

def test_count_words_returns_integer():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert type(test_class.count_words()) == int

'''
Test that the system can return the number of words in the diary just from the contents.
'''

def test_word_count_from_contents():
    test_class = DiaryEntry('','This is some test contents.')
    assert test_class.count_words() == 5

'''
Test that the system can also counts in the words within the title.
'''

def test_word_count_from_title_and_contents():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert test_class.count_words() == 7

'''
Test blank contents returns count of title.
'''
def test_word_count_from_blank_contents():
    test_class = DiaryEntry('Test Title',' ')
    assert test_class.count_words() == 2

'''
Test that the system returns a string for the reading time in minutes.
'''
def test_reading_time_returns_string():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert type(test_class.reading_time(1)) == str

'''
Test that the system returns a string containing the word "minutes." 
'''
def test_reading_time_returns_minutes():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert 'minutes.' in test_class.reading_time(1)

'''
Test that the system can return the correct number of minutes as a float to 2 places.
'''

def test_reading_time_returns_correct_float():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert test_class.reading_time(3) == '2.33 minutes.'

'''
Test that system throws an error when given a number less than 1.
'''

def test_zero_or_negative_wpm_value_throws_error():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    with pytest.raises(Exception) as e:
        test_class.reading_time(-1)
    error_message = str(e.value)
    assert error_message == 'Invalid words per minute. Please try again.'
    with pytest.raises(Exception) as e:
        test_class.reading_time(0)
    error_message = str(e.value)
    assert error_message == 'Invalid words per minute. Please try again.'

'''
Test that the system returns a string from the reading_chunk module.
'''

def test_reading_chunk_returns_string():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert type(test_class.reading_chunk(1,1)) == str

'''
Test that the system tells you that you have no time to read if you put 0 minutes.
'''

def test_no_time_to_read_returns_appropriate_response():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert test_class.reading_chunk(1,0) == 'You have no time to read anything.'

'''
Test that wpm is valid i.e wpm>0 otherwise throw error informing user.
'''

def test_valid_wpm_in_reading_chunk():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    with pytest.raises(Exception) as e:
        test_class.reading_chunk(0,0)
    error_message = str(e.value)
    assert error_message == 'Invalid words per minute. Please try again.'

'''
Test that the title and part of the contents is output when reading chunk is called.
'''

def test_output_contains_title_and_part_of_contents():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert 'Test Title: This' in test_class.reading_chunk(1,3)

'''
Test that the system gives the correct output for a valid wpm and minutes value.
'''

def test_correct_output_given_valid_parameters():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert test_class.reading_chunk(1,3) == 'Test Title: This...'

'''
Test that if the system is called again it will return the next section of text.
'''

def test_multiple_calls_of_reading_chunk_returns_next_chunk():
    test_class = DiaryEntry('Test Title','This is some test contents.')
    assert test_class.reading_chunk(1,3) == 'Test Title: This...'
    assert test_class.reading_chunk(1,3) == '...is some test...'

'''

'''