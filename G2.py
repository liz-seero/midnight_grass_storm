# todo_list.py

import sys

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task added: "{task}"')

    def list_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        print("Your tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index - 1)
            print(f'Task removed: "{removed_task}"')
        except IndexError:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task description: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            todo_list.list_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
