class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.words_to_read = list(self.format().split())

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        if len(self.title) == 0:
            self.title = ' '
        if self.title[-1] == ':':
            return f'{self.title} {self.contents}'
        else:    
            return f'{self.title}: {self.contents}'

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(list(self.contents.split() + self.title.split()))

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        if wpm <= 0:
            raise Exception('Invalid words per minute. Please try again.')
        else:    
            result = round(self.count_words()/wpm,2)
            return f'{result} minutes.'

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        outputtxt = []
        if wpm <=0:
            raise Exception('Invalid words per minute. Please try again.')
        else:
            if minutes == 0:
                return 'You have no time to read anything.'
            for i in range(int(minutes/wpm)):
                outputtxt.append(self.words_to_read.pop(0))
            if outputtxt[0] != list(self.title.split())[0]:
                    outputtxt[0] = '...' + outputtxt[0]
            return ' '.join(outputtxt) + '...'