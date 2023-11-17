# File: lib/diary.py


class DiaryBook:
    def __init__(self):
        self.diary_entries = []
        self.todo_list = None
    def add_diary_entry(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.diary_entries.append(entry)
    def get_diary_entry(self,entry):
        return self.diary_entries[entry-1].format()

    def get_all_diary_entries(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.diary_entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        total = 0
        for entry in self.diary_entries:
            total += entry.count_words()
        return total

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        return int(round(self.count_words()/wpm,0))
    def entries_to_read(self,wpm,minutes):
        
        return_entry = []
        for entry in self.diary_entries:
            result = entry.reading_time(wpm)
            
            if result <= minutes:
                return_entry.append(entry)
        return return_entry

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        return_entry = None
        for entry in self.diary_entries:
            result = entry.reading_time(wpm)
            if result <= minutes:
                if return_entry == None or return_entry.reading_time(wpm) < entry.reading_time(wpm):
                    return_entry = entry
        print(return_entry.contents)    
        return return_entry
    def add_todo_list(self,todo):
        if self.todo_list == None:
            self.todo_list = todo

    def get_all_contacts(self):
        contact_list = []
        for entry in self.diary_entries:
            if entry.display_contact() != None:
                contact_list.append(entry.display_contact())
        return contact_list

    def get_contact(self,entry_number):
        if self.diary_entries[entry_number-1].display_contact() != None:
            return self.diary_entries[entry_number-1].display_contact()
        else:
            return 'There is no contact information.'