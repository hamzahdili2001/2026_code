#!/usr/bin/env python3


def Calculator():
    
    operator_list = ["+", "-", "*", "/"]
    
    number1 = input("Enter Number One: ")
    operator = input("Enter Operator (+, -, *, /): ")
    number2 = input("Enter NUmber Two: ")
    
    
    
    try:
        num1 = float(number1)
        num2 = float(number2)
        
    except ValueError:
        print("One of the numbers is not correct")
        return # stop the function
    
    if operator in operator_list:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
                return
            result = num1 / num2
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print("Operator not correct")

Calculator()

""""
# Another usage
def Calculator():
    # Map operators to lambda functions
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else "Cannot divide by zero"
    }

    number1 = input("Enter Number One: ")
    operator_input = input("Enter Operator (+, -, *, /): ")
    number2 = input("Enter Number Two: ")

    # Convert numbers to float
    try:
        num1 = float(number1)
        num2 = float(number2)
    except ValueError:
        print("One of the numbers is not correct")
        return

    # Calculate using the dictionary
    if operator_input in operations:
        result = operations[operator_input](num1, num2)
        print(f"{num1} {operator_input} {num2} = {result}")
    else:
        print("Operator not correct")

Calculator()

"""