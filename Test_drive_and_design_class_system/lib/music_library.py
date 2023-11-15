class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self.track_list = {}
        pass

    def add(self, track = ''):
        if len(track.strip())  == 0:
            raise Exception("No track entered, please try again")
        self.track_list[track] = "None"
        pass
    
    def search_by_title(self, keyword = ''):
        if len(keyword.strip()) == 0:
            raise Exception( "No keyword given, please try again")
        self.search_results = []
        for key in self.track_list:
            if keyword in key:
                self.search_results.append(f"{key} by {self.track_list[key]}")
        return self.search_results
        