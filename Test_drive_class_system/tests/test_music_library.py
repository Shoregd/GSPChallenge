from lib.music_library import * 
import pytest

"""
class that holds a dictionary of tracks


keeps track of title + artist
when formatting it returns the strings with formats

add

add to dictionary of {artist: title, artist2:title2}


search

search by title for any keyword within title
returns a list


"""


def test_music_library():
    library = MusicLibrary()


def test_add_track_to_music_library():
    library = MusicLibrary()
    assert library.add("Always The Hard Way") == None

def test_track_adds_to_dict():
    library = MusicLibrary()
    library.add("Always The Hard Way")
    assert library.track_list == {"Always The Hard Way":"None"}

def test_second_track_adds_to_dict():
    library = MusicLibrary()
    library.add("Always The Hard Way")
    library.add("Test second track")
    assert library.track_list == {"Always The Hard Way":"None", "Test second track":"None"}

def test_empty_track_returns_error():
    library = MusicLibrary()
    with pytest.raises(Exception) as e:
        library.add("")
    result = str(e.value)
    assert result == "No track entered, please try again"

def test_blank_track_returns_error():
    library = MusicLibrary()
    with pytest.raises(Exception) as e:
        library.add(" ")
    result = str(e.value)
    assert result == "No track entered, please try again"

def test_add_nothing_returns_error():
    library = MusicLibrary()
    with pytest.raises(Exception) as e:
        library.add()
    result = str(e.value)
    assert result == "No track entered, please try again"

def test_search_returns_list():
    library = MusicLibrary()
    assert library.search_by_title('test') == []

def test_return_single_entry():
    library = MusicLibrary()
    library.add("Always The Hard Way")
    library.add("Test second track")
    assert library.search_by_title("Way") == ["Always The Hard Way by None"]

def test_return_multiple_returns():
    library = MusicLibrary()
    library.add("Always The Hard Way")
    library.add("Test second track")
    library.add("Test second track2")
    library.add("Test second track3")
    library.add("Test second track4")
    library.add("Test second track5")
    assert library.search_by_title("Test") == ["Test second track by None", "Test second track2 by None", "Test second track3 by None", "Test second track4 by None", "Test second track5 by None"]

def test_empty_keyword_given():
    library = MusicLibrary()
    library.add("Always The Hard Way")
    with pytest.raises(Exception) as e:
        library.search_by_title('')
    result = str(e.value)
    assert result == "No keyword given, please try again"

def test_blank_keyword_given():
    library = MusicLibrary()
    library.add("Always The Hard Way")
    with pytest.raises(Exception) as e:
        library.search_by_title(' ')
    result = str(e.value)
    assert result == "No keyword given, please try again"


def test_no_keyword_given():
    library = MusicLibrary()
    library.add("Always The Hard Way")
    with pytest.raises(Exception) as e:
        library.search_by_title()
    result = str(e.value)
    assert result == "No keyword given, please try again"