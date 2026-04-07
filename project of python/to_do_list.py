# it's to do list app
to_do_list = []

while True:
    print("Welcome to the To-Do list app!")
    print("please select an operation:")
    print("1. Add a task")
    print("2. view tasks")
    print("3. Delete a task")
    print("4. exit")

    operation = int(input("Enter the number of operation you want to perform:"))
    

    if operation == 4:
        print("Exitting the To-Do list app. Goodbye!")
        break
    elif operation == 1:
        task = input("Enter the task you want to add:")
        to_do_list.append(task)
        print(f"task '{task}' has been added to the list.")
    elif operation == 2:
        if len(to_do_list) == 0:
            print("Your to-do list is empty!!!")
        else:
            print("\n your to-do list:")
            for i, task in enumerate(to_do_list, start=1):
                print(f"{i}. {task}")

            
    elif operation == 3:
        print("error!!!!!")