# This file is the main program for our to-do app

FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    print("\nYour Tasks:")
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(str(i) + ". " + task)

def add_task(tasks):
    new_task = input("Type a new task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added!")

def remove_task(tasks):
    show_tasks(tasks)
    if len(tasks) == 0:
        return

    choice = input("Type the task number to remove: ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print("Removed: " + removed)
        else:
            print("That number is not in the list.")
    else:
        print("Please type a number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose 1, 2, 3, or 4: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Oops! That is not a valid choice.")

main()