def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    if y ==0:
        return "Error! division by zero."
    return x/y
while True:
    print("\n---calculator ---")
    print("1. Add")
    print("2. subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an operation (1-5):")
    
    if choice =='5':
        print("Exiting Calculator.goodbye!")
        break

    num1 = float(input("enter the first number:"))
    num2 = float(input("enter the second number:"))
    
    if choice == '1':
        print("Result:",add(num1,num2))
    elif choice == '2':
        print("Result:",subtract(num1,num2))
    elif choice == '3':
        print("Result:",multiply(num1,num2))
    elif choice == '4':
        print("Result:",divide(num1,num2))
    else:
        print("Invalid input.please select between 1 and 5.")