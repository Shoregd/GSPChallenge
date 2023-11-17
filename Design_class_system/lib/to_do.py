class ToDo:
    def __init__(self):
        self.todo_list = []
        self.completed_list = []
    def add_task(self,task):
        if type(task) != str:
            raise Exception('Task must be a valid string')
        self.todo_list.append(task)
    def show_todo_list(self):
        if self.todo_list == []:
            raise Exception('ToDo list is empty')
        return self.todo_list
    def remove_completed_tasks(self, task):
        if task not in self.todo_list:
            raise Exception('This task is not in the ToDo')
        self.completed_list.append(self.todo_list.pop(self.todo_list.index(task)))
    def show_completed_list(self):
        if self.completed_list == []:
            raise Exception('ToDo list is empty')
        return self.completed_list