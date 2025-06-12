from lib.music_tracker import *
import pytest


def test_given_a_song():
    music_tracker = MusicTracker()
    music_tracker.add_track('Numb')
    assert music_tracker.list_tracks() == ['Numb']


def test_given_two_songs():
    music_tracker = MusicTracker()
    music_tracker.add_track('Numb')
    music_tracker.add_track('Piano Man')
    assert music_tracker.list_tracks() == ['Numb', 'Piano Man']




# '''
# Given an empty string,
# Throw an error
# '''

# music_tracker = MusicTracker()
# music_tracker.add_track('') # == Error 'Invalid Song Name'






# '''
# Given there are no songs in the song list,
# When the list is called, throw an error
# '''

# music_tracker = MusicTracker()
# music_tracker.list_tracks() # == Error 'No Tracks Available, Please add a song using the add_track method'




