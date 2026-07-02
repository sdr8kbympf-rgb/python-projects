todos = []

def add_task(task):
    global todos
    todos.append(task)
    print(f"Added: {task}")

def view_tasks():
    global todos
    if len(todos) == 0:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todos):
            print(f"{i + 1}. {task}")

def remove_task(number):
    global todos
    if number < 1 or number > len(todos):
        print("Invalid number.")
    else:
        removed = todos.pop(number - 1)
        print(f"Removed: {removed}")

while True:
    print("\nWhat do you want to do?")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input ("Enter 1, 2, 3 , or 4,: ")
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        number = int(input("Enter task number to remove: "))
        remove_task(number)
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid choice, try again.")