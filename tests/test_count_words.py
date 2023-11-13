from lib.count_words import *

'''
Test that when emply string is input that the system returns a count of 0
'''

def test_empty_string_returns_0():
    assert count_words('') == 0
'''
Test that the system can count a single word.
'''
def test_single_word_returns_1():
    assert count_words('Taco') == 1
'''
Test that the system can count multiple words.
'''
def test_multiple_words_returns_wordcount():
    assert count_words('Tacos are awesome!') == 3
'''
Test that the system does not recognise empty spaces as a word.
'''
def test_empty_spaces():
    assert count_words('   ') == 0
'''
Test that the system can handle a list of words instead of a string.
'''
def test_list_entry():
    assert count_words(['Tacos','are','awesome']) == 3