from lib.track import *
import pytest
'''
Track is a class that takes 2 string arguments and stores them in a dictionary.
    *It will only allow one track to be stored.
    *No return for init.
    * has a format function to return a string format 'TITLE by ARTIST'

'''

def test_that_title_and_artist_get_assigned():
    test_track = Track('Test Song', 'Test Artist')
    assert test_track.title == 'Test Song'
    assert test_track.artist == 'Test Artist'

'''
Test that init throws an error if title or artist is blank/empty or missing.
'''

def test_error_on_blank_entry():
    with pytest.raises(Exception) as e:
        test_track = Track('Test','')
    error_message = str(e.value)
    assert error_message == 'Title or artist is missing. Please try again.'
    with pytest.raises(Exception) as e:
        test_track = Track('','Test')
    error_message = str(e.value)
    assert error_message == 'Title or artist is missing. Please try again.'
    with pytest.raises(Exception) as e:
        test_track = Track('','')
    error_message = str(e.value)
    assert error_message == 'Title or artist is missing. Please try again.'

def test_error_on_missing_entry():
    with pytest.raises(Exception) as e:
        test_track = Track('Test Track')
    error_message = str(e.value)
    assert error_message == 'Title or artist is missing. Please try again.'


'''
Test that format method returns a string.
'''

def test_format_returns_string():
    test_track = Track('Test Track','Test Artist')
    test_track = Track('Test Track','Test Artist')
    assert type(test_track.format()) == str

'''
Test that format outputs formatted title and artist.
'''

def test_format_outputs_correctly():
    test_track = Track('Test Track','Test Artist')
    assert test_track.format() == 'Test Track by Test Artist'


