from Stack import Stack


class TaskManager:
    def __init__(self):
        self.tasks_dict = dict()

    def new_task(self, task: str, priority: int):
        if priority not in self.tasks_dict:
            self.tasks_dict[priority] = Stack()
        self.tasks_dict[priority].put(task)

    def remove_task(self, task):
        for key in self.tasks_dict.keys():
            if task in self.tasks_dict[key].get_list():
                self.tasks_dict[key].remove(task)
                if self.tasks_dict[key].is_empty():
                    self.tasks_dict.pop(key)
                break

    def __str__(self):
        return '\n'.join([f'{priority} - {"; ".join(self.tasks_dict[priority].get_list())}'
                          for priority in sorted(self.tasks_dict.keys())])
