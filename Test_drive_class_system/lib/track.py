class Track:
    # Public properties:
    #   title: a string
    #   artist: a string

    def __init__(self, title= '', artist= ''):
        # Parameters:
        #   title: a string
        #   artist: a string
        # Side-effects:
        #   Sets the title and artist properties
        if len(title.strip()) == 0 or len(artist.strip()) == 0:
            raise Exception('Title or artist is missing. Please try again.')
        self.title = title
        self.artist = artist

    def format(self):
        # Returns:
        #   a string in the format "TITLE by ARTIST"
        return f'{self.title} by {self.artist}'
