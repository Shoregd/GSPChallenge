from math import ceil, floor

class GrammarStats:
    def __init__(self):
        self.true_count = 0
        self.false_count = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text[0].isupper() and text[-1] in ".?!:":
            self.true_count += 1
            return True
        else:
            self.false_count += 1
            return False
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if (self.true_count + self.false_count) == 0:
            return 100
        else:
            percentage = (self.true_count / (self.true_count + self.false_count)) * 100
            if percentage - int(percentage)  >= .5:
                return int(ceil(percentage))
            else:
                return int(floor(percentage))