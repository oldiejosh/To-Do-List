import datetime
now = datetime.datetime.now()

def greetings():
    print(f"Hello, the time is {now.strftime("%H:%M")}, and the date is {now.date()}")


def add_task():
    to_do = []
    while True:
        task_input = input("Enter task(s) (comma seperated, or type 'done' to finish):")
        if task_input.lower() == "done":
            break
        
        tasks = [t.strip() for t in task_input.split(",") if t.strip()]
        to_do.extend(tasks)
    return to_do


def view_task(tasks):
    if len(tasks) == 0:
        print("Your list is empty")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        


    

def main():
    greetings()
    print("")
    tasks = add_task()
    print("")
    print("To-do:")
    view_task(tasks)
    print("")
    print("End of list.")


main()

