import datetime
now = datetime.datetime.now()

def greetings():
    print(f"Hello, the time is {now.strftime("%H:%M")}, and the date is {now.date()}")


def add_task():
    to_do = []
    task = input("Enter the task:")
    to_do.append(task)


def view_task(tasks):
    if len(tasks == 0):
        print("Your list is empty")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            print("")
            print("End of list.")


    

def main():
    greetings()
    print("")
    add_task()
    print("")
    view_task()


main()

