class Reminder():
    def __init__(self):
        
        self.task_list = []


    def add_task(self,task=None):
        
        if task == None or len(task.strip())==0:
            raise Exception('No task or blank task entered. Please enter valid task.')
        self.task_list.append(task)
        return self.task_list



    def list_tasks(self):
        return self.task_list



    def mark_complete(self,task_number):
        if task_number <= 0:
            raise Exception('Invalid number entered. Please enter a number above 0.')
        if (task_number) > len(self.task_list):
            raise Exception(f'Task {task_number} not in task list. Current task list is {self.task_list}')
        return self.task_list.pop(task_number-1)