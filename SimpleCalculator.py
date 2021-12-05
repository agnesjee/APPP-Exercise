
# Exercise 4,5,7,8
list = []

######## Functions ########
# Arithmetic operation function
def arithmetic(num1, num2):
    operation = int(input("Please select the arithmetic operation you would like to perform:\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n\nYour Choice: "))
    
    if (operation == 1):
        ans = num1 + num2
        string = "addition"
    elif (operation == 2):
        ans = num1 - num2
        string = "substraction"
    elif (operation == 3): 
        ans = num1 * num2
        string = "multiplication"
    else:
        ans = num1 / num2
        string = "division"
    
    list.append(ans)
    print("\nThe " + string + " of the two numbers " + str(num1) + " and " + str(num2) + " is " + str(ans) + "\n")


# Display past answers function
def display():
    if(len(list) == 0):
        print("\nThere is no past answers recorded.\n")
    else:
        print("\nPast Answers:")
        for x in list:
            print(x)
        print("\n")



######## Main body ########
while True:
    print("========")
    print("Welcome to SimpleCalculator! What would you like to start with?")
    print("========")
    choice = int(input("1. Perform Arithmetic Operation\n2. Display all past answer\n3. Exit the program\nYour choice: "))
    
    if (choice == 1):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        arithmetic(num1, num2)
    elif (choice == 2):
        display()
    elif (choice == 3):
        print("\nThank you for using SimpleCalculator! See you next time.")
        break
    else:
        print("\nPlease select a valid option.\n")


