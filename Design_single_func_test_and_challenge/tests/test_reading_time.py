from lib.reading_time import *
import pytest

'''
Test that system can accept a string as the text and not require to be told that
it is a file. Return time to read one word at 200 WPM(Words per minute).
'''
def test_standard_text():
    assert reading_time('Taco') == f'This text will take {round(1/200,2)} minutes to read.' 

'''
Test that system can be told that the text is not a file without throwing an error.
'''
def test_tell_system_istext():
    assert reading_time('Taco',None,False) == f'This text will take {round(1/200,2)} minutes to read.' 

'''
Test that system can return the correct time for a multi-word string.
'''
def test_multiword_string():
    assert reading_time('Tacos are awesome',None,False) == f'This text will take {round(3/200,2)} minutes to read.' 

'''
Test that system can accept a file.
'''
def test_file_acceptance():

    assert reading_time('Test_file.txt',None,True) == f'This text will take {round(3/200,2)} minutes to read.' 

'''
Test that system throws an error when the file does not exist.
'''

def test_file_does_not_exist():
    with pytest.raises(Exception) as e:
        reading_time('This_file_does_not_exist.txt',None,True)
    error_message = str(e.value)
    assert error_message == 'This file does not exist. Please try again.'

'''
Test that the system returns an error when blank data is input.
'''

def test_blank_input():
    with pytest.raises(Exception) as e:
        reading_time(' ',None,False)
    error_message = str(e.value)
    assert error_message == 'No text entered. Please try again.'

'''
Test that the system returns an error when no filename is given.
'''
def test_no_filename():
    with pytest.raises(Exception) as e:
        reading_time(' ',None,True)
    error_message = str(e.value)
    assert error_message == 'No filename given. Please try again.'

'''
Test larger file with spaces still as the delimeter.
'''
def test_larger_file():
    assert reading_time('Test_file_larger.txt',None,True) == f'This text will take {round(36/200,2)} minutes to read.' 

'''
Test system can handle multi line text files correctly
'''
def test_multiline_file():
    assert reading_time('Test_multiline_file.txt',None,True) == f'This text will take {round(3/200,2)} minutes to read.' 

'''
Test system can handle different delimiter. i.e Words seperated by ; like in a CSV file.
'''
def test_delimeter_text():
    words = ''
    for i in range(599):
        words += 'a;'
    assert reading_time(words,';',False) == 'This text will take 3.0 minutes to read.' 
'''
Test system can handle files with different delimeter.
'''
def test_file_delimeter():
    output = open('Test_delimeter_file.txt','w')
    words = ''
    for i in range(599):
        words += 'a;'
    output.write(words)
    output.close()

    assert reading_time('Test_delimeter_file.txt',';',True) == 'This text will take 3.0 minutes to read.'