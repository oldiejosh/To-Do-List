from date import run_date
from greet import greetings
from menu import menu_select
from task_functions import add_task, remove_task, view_task

def main():
    run_date()
    greetings()
    tasks = []

    while True:
        menu_select()
        choice = input("Select your choice:").strip().lower()
        print("")

        if choice == "1":
                new_tasks = add_task()
                tasks.extend(new_tasks)
                print("")

        elif choice == "2":
                view_task(tasks)
                print("End of list.")
        
        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            print("Goodbye")
            break

        else:
             print("Invalid input. Please choose 1, 2, 3, or 4")
        

main()

