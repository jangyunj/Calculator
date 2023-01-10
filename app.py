def add(a, b):
    answer = a + b
    print(f'{a} + {b} = {answer}\n')

def subtract(a, b):
    answer = a - b
    print(f'{a} - {b} = {answer}\n')  

def multiply(a, b):
    answer = a * b
    print(f'{a} * {b} = {answer}\n')

def divide(a, b):
    answer = a / b
    print(f'{a} / {b} = {answer}\n')

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Enter your choice: ")

    if choice.upper() == 'A':
        print("---Addition---")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a, b)
    elif choice.upper() == 'B':
        print("--Subtraction--")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        subtract(a, b)
    elif choice.upper() == 'C':
        print("--Multiplication--")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        multiply(a, b)
    elif choice.upper() == 'D':
        print("--Division--")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        divide(a, b)
    else:
        print("Program ended")
        quit()

