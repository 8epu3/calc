from calculator.operations import *

while True:
    print("a. Add")
    print("s. Substract")
    print("m. Multiply")
    print("d. Divide")
    print("q. Quit")
    print()

    op = input("Enter option: ")
    print()

    if op == 'q':
        print("Good-bye")
        break
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print()

    if op == 'a':
        print("Result", add(a, b))
        print()
    elif op == 's':
        print("Result", sub(a, b))
        print()
    elif op == 'm':
        print("Result", mul(a, b))
        print()
    elif op == 'd':
        print("Result", div(a, b))
        print()
    else:
        print("Learn to read")
