import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def square(a):
    return a * a

def square_root(a):
    return math.sqrt(a)

def cube(a):
    return a * a * a

def cube_root(a):
    return a ** (1/3)


def main():
    print("Welcome to the calculator!")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Cube")
    print("8. Cube Root")
    print("9. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(add(a, b))
    elif choice == 2:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(subtract(a, b))
    elif choice == 3:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(multiply(a, b))