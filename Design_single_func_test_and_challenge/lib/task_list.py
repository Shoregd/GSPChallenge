'''
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

Parameters:
    Function will accept a string as an argument to then return a boolean if a task was found.

Side-Effects:
    Function will return a boolean for if a task is found or not. No printing will be
    done at this stage
'''
def task_list(text):
   check_text = '#TODO'
   allowed_seperator = '_-/ '
   check_letter_count = 0
   for letter in text:
        if letter in allowed_seperator:
            pass
        else:

            if letter == check_text[check_letter_count]:
                check_letter_count +=1
            else:
                check_letter_count = 0
            if check_letter_count == 5:
                return True
    
    
   
   return False