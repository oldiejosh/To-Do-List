from date import run_date
from greet import greetings
from add import add_task
from view import view_task

def main():
    run_date()
    greetings()
    tasks = add_task()
    print("")
    print("To-do:")
    view_task(tasks)
    print("End of list.")


main()

