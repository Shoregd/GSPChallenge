from lib.grammar_check import *
import pytest
'''
Test that the system returns true when valid text is given.
'''
def test_valid_text():
    assert grammar_check('Tacos.') == True

'''
Test that the system return an error when there is no puntuation at the end of the 
sentence.
'''

def test_error_on_no_punctuation():
    with pytest.raises(Exception) as e:
        grammar_check('Tacos')
    error_message = str(e.value)
    assert error_message == 'Text is missing ending punctuation.'

'''
Test the system returns error of no capitalisation at start of text.
'''
def test_no_cap_at_start():
    with pytest.raises(Exception) as e:
        grammar_check('tacos.')
    error_message = str(e.value)
    assert error_message == 'Text is missing capital letter at the start of text.'
'''
Test that system can handle multiple sentences where they are both valid.
'''   
def test_valid_multi_sentence_text():
    assert grammar_check('Tacos.Are.Awesome.') == True

'''
Test that the system can handle blank input
'''
def test_blank_input():
    with pytest.raises(Exception) as e:
        grammar_check(' ')
    error_message = str(e.value)
    assert error_message == 'Blank text entered. Please provide text.'
'''
Test that system can handle different VALID punctuation i.e !, ?, ., ..., : 
'''
def test_other_punctuation():
    assert grammar_check('Tacos!') == True
    assert grammar_check('Tacos?') == True
    assert grammar_check('Tacos...') == True
    assert grammar_check('Tacos:') ==True

'''
Extension activity.
Test that the system can recognise when one of the sentences is invalid.
'''

def test_missing_cap_multi_sentence_text():
    with pytest.raises(Exception) as e:
        grammar_check('Tacos.are.Awesome.')
    error_message = str(e.value)
    assert error_message == 'Text is missing capital letter at the start of a sentence.'

'''
Test that system can recognise when missing punctuation in sentence(not last sentence)
'''

def test_missing_punc_multi_sentence_text():
    with pytest.raises(Exception) as e:
        grammar_check('TacosAre.Awesome.')
    error_message = str(e.value)
    assert error_message == 'Text is missing punctuation.'