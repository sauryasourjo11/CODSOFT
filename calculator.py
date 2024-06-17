# Define a function to perform addition
def add(x, y):
    return x + y

# Define a function to perform subtraction
def subtract(x, y):
    return x - y

# Define a function to perform multiplication
def multiply(x, y):
    return x * y

# Define a function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main function to take input from the user and perform the chosen operation
def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter choice(1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Input")

# Run the calculator
calculator()
