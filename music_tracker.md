# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user

So that I can keep track of my music listening

I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Create an empty list to store the songs
        #   self.music_storage = []
        pass # No code here yet

    def add_track(self, song):
        # Parameters:
        #   string: Song name
        # Returns:
        #   Nothing
        # Side-effects
        #   Adds the song to the music_storage list
        pass # No code here yet

    def list_tracks(self):
        # Returns:
        #   Music storage list
        # Side-effects:
        #   None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a song,
It should add the song to the music_storage list
"""

music_tracker = MusicTracker()
music_tracker.add_track('Numb')
music_tracker.list_tracks() # == ['Numb']

'''
Given 2 songs,
It should add both the songs to the list
'''

music_tracker = MusicTracker()
music_tracker.add_track('Numb')
music_tracker.add_track('Piano Man')
music_tracker.list_tracks() # == ['Numb','Piano Man']

'''
Given an empty string,
Throw an error
'''

music_tracker = MusicTracker()
music_tracker.add_track('') # == Error 'Invalid Song Name'

'''
Given there are no songs in the song list,
When the list is called, throw an error
'''

music_tracker = MusicTracker()
music_tracker.list_tracks() # == Error 'No Tracks Available, Please add a song using the add_track method'

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
