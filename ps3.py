def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "An error occured!!"
    return x/y

def calculator():
    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multply")
    print("4. Divide")

    choice = input("Enter your Choice (1/2/3/4): ")

    num1 = float(input("Enter 1st value:"))
    num2 = float(input("Enter 2nd value:"))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1,num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1,num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1}/{num2} = {divide(num1, num2)}")
    else:
        print("Invalid Input")

calculator()