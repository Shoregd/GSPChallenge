from lib.design_a_class_exercise import *
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

'''
Test that class returns a list when a task is added.
'''

def test_add_task_returns_list():
    test_class = Reminder()
    assert type(test_class.add_task('Test Task')) == list

'''
Test that add task returns the held task list.
'''

def test_add_task_returns_task_list():
    test_class = Reminder()
    assert test_class.add_task('Test Task') == test_class.task_list

'''
Test that add task updates the task list.
'''

def test_add_task_updates_task_list():
    test_class = Reminder()
    test_class.add_task('Test Task')
    assert test_class.task_list[0] == 'Test Task'

'''
Test that add task updates the task list with multiple entries.
'''

def test_add_multiple_tasks():
    test_class = Reminder()
    test_class.add_task('Test Task 1')
    test_class.add_task('Test Task 2')
    test_class.add_task('Test Task 3')
    test_class.add_task('Test Task 4')
    assert test_class.task_list == ['Test Task 1','Test Task 2','Test Task 3','Test Task 4']

'''
Test that add task throws an error when no text is sent as the task.
'''

def test_error_thrown_for_no_text():
    test_class = Reminder()
    with pytest.raises(Exception) as e:
        test_class.add_task()
    error_message = str(e.value)
    assert error_message == 'No task or blank task entered. Please enter valid task.'

'''
Test that add task throws an error for an empty string or blank string is entered.
'''

def test_error_thrown_for_empty_or_blank_text():
    test_class = Reminder()
    with pytest.raises(Exception) as e:
        test_class.add_task('')
    error_message = str(e.value)
    assert error_message == 'No task or blank task entered. Please enter valid task.'
    test_class = Reminder()
    with pytest.raises(Exception) as e:
        test_class.add_task(' ')
    error_message = str(e.value)
    assert error_message == 'No task or blank task entered. Please enter valid task.'


'''
Test that list tasks returns a list.
'''

def test_list_task_returns_list():
    test_class = Reminder()
    assert type(test_class.list_tasks()) == list

'''
Test that list tasks returns the current task list when task list is empty.
'''

def test_list_task_returns_task_list():
    test_class = Reminder()
    assert test_class.list_tasks() == test_class.task_list

'''
Test that list tasks returns current task list with tasks added.
'''

def test_list_tasks_returns_task_list_with_added_tasks():
    test_class = Reminder()
    test_class.add_task('Test Task 1')
    assert test_class.list_tasks() == ['Test Task 1']
    test_class.add_task('Test Task 2')
    assert test_class.list_tasks() == ['Test Task 1','Test Task 2']
    test_class.add_task('Test Task 3')
    assert test_class.list_tasks() == ['Test Task 1', 'Test Task 2','Test Task 3']
    test_class.add_task('Test Task 4')
    assert test_class.list_tasks() == ['Test Task 1', 'Test Task 2', 'Test Task 3', 'Test Task 4']

'''
Test mark complete returns a string.
'''

def test_mark_complete_returns_string():
    test_class = Reminder()
    test_class.add_task('Test Task 1')
    test_class.add_task('Test Task 2')
    assert type(test_class.mark_complete(1)) == str

'''
Test that system returns a task from the task list when provided with a valid task number.
'''

def test_valid_task_returned():
    test_class = Reminder()
    test_class.add_task('Test Task 1')
    test_class.add_task('Test Task 2')
    test_class.add_task('Test Task 3')
    test_class.add_task('Test Task 4')
    assert test_class.mark_complete(1) in ['Test Task 1', 'Test Task 2', 'Test Task 3', 'Test Task 4']

'''
Test that mark complete returns the correct task when given a valid input.
'''

def test_mark_complete_returns_correct_task():
    test_class = Reminder()
    test_class.add_task('Test Task 1')
    test_class.add_task('Test Task 2')
    test_class.add_task('Test Task 3')
    test_class.add_task('Test Task 4')
    assert test_class.mark_complete(1) == 'Test Task 1'

'''
Test that completed valid task is removed from the task list.
'''

def test_mark_complete_removes_valid_task():
    test_class = Reminder()
    test_class.add_task('Test Task 1')
    test_class.add_task('Test Task 2')
    test_class.add_task('Test Task 3')
    test_class.add_task('Test Task 4')
    assert test_class.mark_complete(1) not in test_class.task_list

'''
Test that mark complete throws an error when task asked to be removed that is larger than the current task list.
'''

def test_mark_complete_throws_error_for_task_number_larger_than_current_list():
    test_class = Reminder()
    test_class.add_task('Test Task 1')
    test_class.add_task('Test Task 2')
    test_class.add_task('Test Task 3')
    test_class.add_task('Test Task 4')
    with pytest.raises(Exception) as e:
        test_class.mark_complete(5)
    error_message = str(e.value)
    assert error_message == f'Task 5 not in task list. Current task list is {test_class.task_list}'

'''
Test that mark complete throws an error when invalid number is entered i.e tasknumber <=0.
'''

def test_mark_complete_throws_error_for_invalid_number():
    test_class = Reminder()
    test_class.add_task('Test Task 1')
    test_class.add_task('Test Task 2')
    test_class.add_task('Test Task 3')
    test_class.add_task('Test Task 4')
    with pytest.raises(Exception) as e:
        test_class.mark_complete(0)
    error_message = str(e.value)
    assert error_message == 'Invalid number entered. Please enter a number above 0.'
