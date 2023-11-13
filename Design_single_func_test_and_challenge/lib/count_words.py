def count_words(text):
    if type(text) == str:
            
        wordlist = text.split()
        return len(wordlist)
    else:
        return len(text)