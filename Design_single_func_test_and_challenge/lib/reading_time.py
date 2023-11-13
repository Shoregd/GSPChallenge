import os
'''
In this exercise we have to write a program that will let us estimate
the amount of time it will take to read a given text. 
This assumes that the reader can read 200 words per minute.

Parameters: 
    Function will accept a string or file to be read.
It will also take a boolean to tell it if the given text is a file
or string. System will default to assume that text is a string if
not informed otherwise. EDIT: System will also accept a delimiter to tell it what 
character will seperate the words within the file.

Returns: 
    A string containing the number of minutes and a statement
to assure user of value of unit i.e "This text will take 177 minutes
to read"
If the filename provided does not exist it will return that the specified
file does not exist and ask the user to check their input.
If no file or text is provided it will return an error asking for input.

Side effects: 
    This function will return information back to the user or provide an
    error message with how to resolve the problem. Nothing will be printed.
'''
def reading_time(file_or_text,delimiter= ' ',isfile=False):
    if len(file_or_text.strip()) == 0:
        if isfile:
            raise Exception('No filename given. Please try again.')
        else:
            raise Exception('No text entered. Please try again.')
    else:
        if isfile:
        

            if os.path.exists(file_or_text):
                    
                output = open(file_or_text,'r')
                outputtxt = output.read()
                word_hold = outputtxt.split(delimiter)
                output.close()
            else:
                raise Exception('This file does not exist. Please try again.')
        else:                    
                word_hold = file_or_text.split(delimiter)             
    
    return_value = round((len(word_hold)/200),2)
    return f'This text will take {return_value} minutes to read.'