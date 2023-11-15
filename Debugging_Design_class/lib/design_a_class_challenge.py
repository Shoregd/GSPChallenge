class My_Music():
    def __init__(self):
        self.song_list = []
    
    def add_song(self,track_name = None):
        if track_name == None or len(track_name.strip()) == 0:
            raise Exception('No track name given. Please try again.')
        if track_name in self.song_list:
            raise Exception(f'Song already added. Please add different song not in {self.song_list}.')
        self.song_list.append(track_name)
        return self.song_list

    def list_songs(self):
        return self.song_list