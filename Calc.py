# Calculator
#This program will create a simple calculator
#for addition, subtraction, multiplication, division
#7.9.2023

#Addition
def add(x, y):
    return x + y

#Subtraction
def subtract(x, y):
    return x - y

#Multiplication
def multiply(x, y):
    return x * y

#Division
def divide(x, y):
    return x / y

#Main Run

#Prompt user to select the calculator operation
print("Choose the operation to calculate")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divison")

#While loop to take the user's input
while True:
    userInput = input("Enter your selection(1, 2, 3, 4): ")
    
    #Check if the selection is one of the valid options
    if userInput in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if userInput == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            
        elif userInput == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            
        elif userInput == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            
        elif userInput == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    
        #Check if the user wants to continue calculating
        #If the answer is no, break the loop to exit
        continueCalc = input("Would you like to perform another calculation? (y/n):")
        if continueCalc == 'n':
            break
        
    else:
        print("Invalid Input")
            
        