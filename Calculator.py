import math 


def Calculator():
    first = input("Please input a number \n")
    first = int(first)
    second = input("Please enter another number or type pi \n")
    if second == "pi":
        second = math.pi
    else:
        second = int(second)
    operation = input("Please enter a operation (+, -, /, *, ^): \n")
    result = 0
    if type(operation) == str:
        if operation == "+":
            result = first + second
            return print(first, operation, second, "=", result)
        elif operation == "-":
            result = first - second
            return print(first, operation, second, "=", result)
        elif operation == "*":
            result = first * second
            return print(first, operation, second, "=", result)
        elif operation == "/":
            result = first / second
            return print(first, operation, second, "=", result)
        elif operation == "^":
            result = pow(first,second)
            return print(first,operation,second, "=", result)
        else:
            print("Error! operation is invalid")
            return
    else:
        print("Error, operator wasn't inputed as string, Please input a string (+) ")


Calculator()
