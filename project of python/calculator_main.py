# Calculator main file
while True:


 print("Welcome to the calculator!")
 print("please select an operation:")  
 print("1. Addition")
 print("2. Subtraction")
 print("3. Multiplication")
 print("4. Division")
 print("5. Exit")
 operation = int(input("Enter the number of the operation you want to perform: "))
 dict_operations = {1: "Addition", 2: "Subtraction", 3: "Multiplication", 4: "Division", 5: "Exit"}
 if operation in dict_operations:
    print(f"You have selected {dict_operations[operation]}")

  
    if operation ==5:
        print("Exitin the calculator,,,,Good bye!!")
        break
    else: 
     num1 = float(input("Enter the first number: "))
     num2 = float(input("Enter the second number: "))
    
     if operation == 1:
        result = num1 + num2
        print(f"The result of {num1}+ {num2} is : {result}")
     elif operation == 2:
        result = num1 - num2 
        print(f"The result of {num1}- {num2} is : {result}")
     elif operation == 3:
        result = num1 * num2
        print(f"The result of {num1}* {num2} is : {result}")
     elif operation ==4:
        if num2 != 0:
            result = num1/num2
            print(f"The result of {num1}/ {num2} is : {result}")
        else:
            print("Error!! Division by zero is Math error")
    
    
