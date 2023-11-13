import string
'''
Problem:
As a user
So that I can improve my grammar I want to verify that a text starts
with a capital letter and ends with a suitable sentence-ending punctuation mark.

Parameters:
    The function will accept a variable 'text' as a string. The function will not
    initially test for multi-sentance strings. Potential extension activity.

Returns:
    The function will return true if the text passes or an error outlying the issue.

Side-effects:
    There will be no printing to the screen only the boolean or error message.
'''

def grammar_check(text):
    cap_alpha = string.ascii_uppercase
    valid_punc = '!?.:...'
    text_list = ''
    iscap = True
    ispunc = False
    if len(text.strip()) ==0:
        raise Exception('Blank text entered. Please provide text.')
    else:
            
        if text[0] in cap_alpha:
                
            if text[-1] in valid_punc:
                
                text_list = text[1:]
                for place in range(len(text_list)):
                    
                    if text_list[place] in valid_punc and iscap == False:
                        if text_list[place:(place+3)] == '...':
                            if place + 3 == len(text_list):
                                return True
                            
                        else:    
                            raise Exception('Text is missing capital letter at the start of a sentence.')
                    elif text_list[place] in valid_punc and iscap == True:
                        
                        if text_list[place:(place+3)] == '...':
                           
                            
                            if place + 3 == len(text_list):
                                return True
                            
                        iscap = False
                    elif text_list[place] in cap_alpha and iscap == False:
                        iscap = True
                    elif text_list[place] in cap_alpha and iscap == True:
                        raise Exception('Text is missing punctuation.')
                return True
                    
            else:
                raise Exception('Text is missing ending punctuation.')
        else:
            raise Exception('Text is missing capital letter at the start of text.')
        
        
