from lib.design_a_class_challenge import *
import pytest
'''
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

Class will be called My_Music():

    * Class will need to hold a list of the currently held songs.
    * Class will need a method to add a track.
    * Class will output the new list after a song is added.
    * Class will need a method to list the songs that have been added.
    * Class will not allow duplicate songs to be added.
    * Class will not allow a blank song to be added.
'''

'''
Test that class initialises with a blank song list.
'''

def test_class_init_has_blank_song_list():
    test_class = My_Music()
    assert test_class.song_list == []

'''
Test that add song method returns a list.
'''

def test_add_song_returns_type_list():
    test_class = My_Music()
    assert type(test_class.add_song('Test')) == list

'''
Test that add song can accept a string as the song name. Default to None if no track text entered.
'''

def test_add_song_accepts_string():
    test_class = My_Music()
    assert test_class.add_song("Test Track") == test_class.song_list

'''
Test that add song actually adds the track to the song list.
'''

def test_add_song_adds_song_to_list():
    test_class = My_Music()
    test_class.add_song('Test Track')
    assert 'Test Track' in test_class.song_list

'''
Test that multiple songs can be added.
'''

def test_add_song_adds_multiple_songs():
    test_class = My_Music()
    test_class.add_song('Test Track')
    assert 'Test Track' in test_class.song_list
    test_class.add_song('Test Track 1')
    assert 'Test Track 1' in test_class.song_list
    test_class.add_song('Test Track 2')
    assert 'Test Track 2' in test_class.song_list
    test_class.add_song('Test Track 3')
    assert 'Test Track 3' in test_class.song_list

'''
Test that add song returns an error that a song is already in the list.
'''

def test_add_song_throws_error_on_duplicate_song():
    test_class = My_Music()
    test_class.add_song('Test Track')
    with pytest.raises(Exception) as e:
        test_class.add_song('Test Track')
    error_message = str(e.value)
    assert error_message == f'Song already added. Please add different song not in {test_class.song_list}.'

'''
Test that add song throws an error when no track text has been given.
'''

def test_add_song_no_text_given():
    test_class = My_Music()
    with pytest.raises(Exception) as e:
        test_class.add_song()
    error_message = str(e.value)
    assert error_message == 'No track name given. Please try again.'

'''
Test that add song throws an error when empty or blank string is entered.
'''

def test_add_song_blank_or_empty_text():
    test_class = My_Music()
    with pytest.raises(Exception) as e:
        test_class.add_song('')
    error_message = str(e.value)
    assert error_message == 'No track name given. Please try again.'
    with pytest.raises(Exception) as e:
        test_class.add_song('  ')
    error_message = str(e.value)
    assert error_message == 'No track name given. Please try again.'

'''
Test that list songs returns a list.
'''

def test_list_songs_returns_list():
    test_class = My_Music()
    assert type(test_class.list_songs()) == list

'''
Test that list songs returns the current song list.
'''

def test_list_songs_returns_current_song_list():
    test_class = My_Music()
    test_class.add_song('Test Track')
    assert test_class.list_songs() == test_class.song_list
    test_class.add_song('Test Track 1')
    assert test_class.list_songs() == test_class.song_list
    test_class.add_song('Test Track 2')
    assert test_class.list_songs() == test_class.song_list
    test_class.add_song('Test Track 3')
    assert test_class.list_songs() == test_class.song_list