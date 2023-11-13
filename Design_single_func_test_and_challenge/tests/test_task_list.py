from lib.task_list import *
import pytest

'''
Test that function returns false for empty string
'''
def test_empty_string():
    assert task_list('') == False
'''
Test that functino can return true if input valid.
'''
def test_valid_input():
    assert task_list('#TODO Some random task.') == True

'''
Test that function can regognise to do appended instead of prepended.
'''

def test_append_validity():
    assert task_list('Some random task. #TODO')

'''
Test system returns false for invalid input
'''

def test_invalid_input():
    assert task_list('Some random task.') == False

'''
Test that if check phrase is not together it still returns false.
'''
def test_space_in_validity():
    assert task_list('#TO Some random task. DO') == False

'''
Test that the system allows spacing between validity i.e #TO DO
'''
def test_spaced_validator():
    assert task_list('#TO DO Some random task.') == True

'''
Test that the system can handle a single item seperator i.e _,-,/, . Cannot have # as
allowed space as it is also in the check.
'''
def test_single_seperator():
    assert task_list('#TO_DO Some random task.') == True
    assert task_list('#TO-DO Some random task.') == True
    assert task_list('#TO/DO Some random task.') == True
    
    