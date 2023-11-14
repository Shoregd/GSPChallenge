from lib.design_a_class import *
import pytest
'''
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

Notes:
    * Class will need modules: __init__, add_task, list_tasks, complete_task
    * Class will need to hold current task list and be accessible to multiple methods
    * Class will need to return lists to the user
    * Class will need to remove items from the list 

'''

'''
Test initialisation of class with a blank task list.
'''

def test_init_of_class():
    test_class = Reminder()
    assert test_class.task_list == []
