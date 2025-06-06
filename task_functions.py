def view_task(tasks):
    if not tasks:
        print("Your list is empty")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(existing_tasks=None):
    if existing_tasks is None:
        existing_tasks= []

    while True:
        task_input = input("Enter task(s) *comma seperated* when finished type 'done':")
        if task_input.lower() == "done":
            break
        
        tasks = [t.strip() for t in task_input.split(",") if t.strip()]
        existing_tasks.extend(tasks)
        print("")
        print("Current to-do list:")
        for i, task in enumerate(existing_tasks, 1):
            print(f"{i}. {task}")
    return existing_tasks


def remove_task(tasks):
    while True:
        if not tasks:
            print("Your list is empty, nothing to remove.")
            break

        print("\n current to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        removed_input = input("type the number(s) of the task(s) to remove (or 'done' to finish):")
        if removed_input.lower() == "done":
            break

        indexes = [int(i.strip()) - 1 for i in removed_input.strip(",") if i.strip().isdigit()]

        for index in indexes:
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Removed: {removed}")
            else:
                print(f"Removed: '{removed}")
