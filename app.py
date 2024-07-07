
print('''
     To-Do List Application 
     --------------------
     1. Add To-Do-List
     2. See To-Do-List
     3. Delete from list 
     4. Quite
     --------------------
''')

todo = []


def add():
    added = input(' Enter a task to add to the to-do list: ')
    if added.strip():  # to check whether it's empty
        if added not in todo:
            todo.append(added)
            print(f" '{added}' has been added to the list. ")
        else:
            print(f"'{added}' already in the list. ")
    else:
        print('Enter a non empty item. ')


def see():
    # to check whether the index exist in the list
    try:
        index = int(input('Enter the index of the list: '))
        if 0 <= index < len(todo):
            print(f'Task at index {index}: {todo[index - 1]}')
        else:
            print("Invalid index. Please enter a valid index ")
    except ValueError:
        print("Invalid input. Please enter a valid integer index.")


def delete():
    try:
        index = int(input('Enter the index of the task you want to delete: '))
        if 0 <= index < len(todo):
            deleted_task = todo.pop(index)
            print(f"Task '{deleted_task}' at index {index} has been removed.")
        else:
            print("Invalid index. Please enter a valid index ")
    except ValueError:
        print("Invalid input. Please enter a valid integer index.")


while True:
    pick = int(input('Pick an option: '))
    if pick == 1:
        add()
    elif pick == 2:
        see()
    elif pick == 3:
        delete()
    elif pick == 4:
        print("You've exited")
        break
    else:
        print("Invalid index. Please enter a valid index ")
