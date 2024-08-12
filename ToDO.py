import os

# File to store the tasks
TODO_FILE = 'tasks.txt'

def add_task(task):
    with open(TODO_FILE, 'a') as file:
        file.write(task + '\n')
    print(f'Task "{task}" added.')

def view_tasks():
    if not os.path.exists(TODO_FILE):
        print('No tasks found.')
        return

    with open(TODO_FILE, 'r') as file:
        tasks = file.readlines()
    if tasks:
        print('Your tasks:')
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task.strip()}')
    else:
        print('No tasks found.')

def delete_task(task_number):
    if not os.path.exists(TODO_FILE):
        print('No tasks to delete.')
        return

    with open(TODO_FILE, 'r') as file:
        tasks = file.readlines()

    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        with open(TODO_FILE, 'w') as file:
            file.writelines(tasks)
        print(f'Task "{removed_task.strip()}" deleted.')
    else:
        print('Invalid task number.')

def main():
    while True:
        print('\nTo-Do List')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Delete Task')
        print('4. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            task = input('Enter the task: ')
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_number = int(input('Enter task number to delete: '))
                delete_task(task_number)
            except ValueError:
                print('Please enter a valid number.')
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()