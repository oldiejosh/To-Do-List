def view_task(tasks):
    if not tasks:
        print("Your list is empty")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
