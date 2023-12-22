from Stack import Stack
from TaskManager import TaskManager

print('Задача 5. Стек\n')

stack = Stack()
stack.put(1)
stack.put(2)
stack.put(3)

print(stack)

while True:
    last_item = stack.get()
    print(last_item)
    print(stack)
    if last_item is None:
        break

manager = TaskManager()

manager.new_task("сделать уборку", 4)

manager.new_task("помыть посуду", 4)

manager.new_task("отдохнуть", 1)

manager.new_task("поесть", 2)

manager.new_task("сдать ДЗ", 2)

print(manager)

manager.remove_task('поесть')
manager.remove_task('отдохнуть')

print(manager)

