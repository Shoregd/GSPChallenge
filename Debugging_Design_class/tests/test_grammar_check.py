from lib.grammar_check import *
import pytest

'''
Not testing initialisation as no parameters
'''

'''
Testing check function returning boolean value
'''
def test_check_returns_bool():
    grammar_stats = GrammarStats()
    assert type(grammar_stats.check("something")) == bool
    
'''
Testing correct response for valid input
'''
def test_check_valid_input_is_true():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Something.") == True
    
'''
Testing correct response for invalid input
'''
def test_check_capital_letter_at_start():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("something.") == False
    
def test_check_missing_punctuation():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Something") == False
    
def test_check_missing_punctuation_and_capital():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("something") == False
    
"""
Testing other sentence-ending punctuations
"""    
def test_check_includes_other_punctuation():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Something?") == True
    assert grammar_stats.check("Something!") == True
    assert grammar_stats.check("Something:") == True
    
'''
Testing to see if percertage_good returns an int
'''
def test_percentage_good_returns_int():
    grammar_stats = GrammarStats()
    assert type(grammar_stats.percentage_good()) == int
    
'''
Testing to see if returns 100% when all checks are good
'''    
def test_percentage_good_all_true():
    grammar_stats = GrammarStats()
    grammar_stats.check("Something?")
    grammar_stats.check("Something!")
    grammar_stats.check("Something:")
    assert grammar_stats.percentage_good() == 100
    
'''
Testing to see if returns 0% when all checks are bad
'''    
def test_percentage_good_all_false():
    grammar_stats = GrammarStats()
    grammar_stats.check("Something")
    grammar_stats.check("Something")
    grammar_stats.check("Something")
    assert grammar_stats.percentage_good() == 0
    
'''
Testing to see if returns 50% when half fail
'''
def test_percentage_good_half_false():
    grammar_stats = GrammarStats()
    grammar_stats.check("Something?")
    grammar_stats.check("Something!")
    grammar_stats.check("Something")
    grammar_stats.check("Something")
    assert grammar_stats.percentage_good() == 50
    
'''
Testing to see if returns 33% when 2/3 test fail
'''
def test_percentage_good_a_third_pass():
    grammar_stats = GrammarStats()
    grammar_stats.check("Something")
    grammar_stats.check("Something")
    grammar_stats.check("Something!")
    assert grammar_stats.percentage_good() == 33
    
'''
Testing to see if returns 67% when 2/3 test pass
'''
def test_percentage_good_a_third_fail():
    grammar_stats = GrammarStats()
    grammar_stats.check("Something")
    grammar_stats.check("Something!")
    grammar_stats.check("Something!")
    assert grammar_stats.percentage_good() == 67  
    
'''
Testing to see if returns 13% when 1/8 tests pass
'''
def test_percentage_good_an_eigth_pass():
    grammar_stats = GrammarStats()
    grammar_stats.check("Something")
    grammar_stats.check("Something!")
    grammar_stats.check("Something")
    grammar_stats.check("Something")
    grammar_stats.check("Something")
    grammar_stats.check("Something")
    grammar_stats.check("Something")
    grammar_stats.check("Something")
    assert grammar_stats.percentage_good() == 13  