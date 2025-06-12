class MusicTracker:

    def __init__(self):
        self.music_tracker = []
    
    def add_track(self,song):
        if len(song) == 0:
            raise Exception('Invalid Song Name')
        self.music_tracker.append(song)

    def list_tracks(self):
        
        return self.music_tracker

