def add_task(existing_tasks=None):
    if existing_tasks is None:
        existing_tasks= []

    while True:
        task_input = input("Enter task(s) *comma seperated* when finished type 'done':")
        if task_input.lower() == "done":
            break
        
        tasks = [t.strip() for t in task_input.split(",") if t.strip()]
        existing_tasks.extend(tasks)

        print("Current to-do list:")
        for i, task in enumerate(existing_tasks, 1):
            print(f"{i}. {task}")
        print("")
    return existing_tasks
