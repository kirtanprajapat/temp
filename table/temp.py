# Define the to-do list as an empty list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f'Added task: {task}')

# Function to remove a task from the to-do list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f'Removed task: {task}')
    else:
        print(f'Task not found: {task}')

# Function to view all tasks in the to-do list
def view_tasks():
    if todo_list:
        print("To-Do List:")
        for index, task in enumerate(todo_list, 1):
            print(f'{index}. {task}')
    else:
        print("To-Do List is empty.")

# Function to clear all tasks in the to-do list
def clear_tasks():
    todo_list.clear()
    print("Cleared all tasks.")

# Example usage

#To add task
add_task(input("Enter the task:"))
view_tasks()

#To remove task
add_task.re