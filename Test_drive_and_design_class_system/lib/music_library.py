class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self.track_list = []
        pass

    def add(self, track = None):
        if track  == None:
            raise Exception("No track entered, please try again")
        self.track_list.append(track)
        pass
    
    def search_by_title(self, keyword = ''):
        if len(keyword.strip()) == 0:
            raise Exception( "No keyword given, please try again")
        self.search_results = []
        for tracks in self.track_list:
            if keyword in tracks.title:
                self.search_results.append('Hello')
        return self.search_results
        