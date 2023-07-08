from calculator_ascii_art import calculator_art, calculator_image


# method 1

# def operation(operator, num1, num2):
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         return num1 / num2
#     else:
#         return

# method 2


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

arthimetic_symbols = """
+
-
*
/
"""


def calculator():
    print(calculator_art, calculator_image)
    operand1 = float(input("Enter the first number: "))
    check = True
    print(arthimetic_symbols)
    while check:
        sign = input("Pick the operator: ")
        operand2 = float(input("Enter the second number: "))

        function = operation[sign]
        result = function(operand1, operand2)
        # result = operation(sign, operand1, operand2)

        print("{0:.1f} {1} {2:.1f} = {3:.1f}".format(operand1, sign, operand2, result))
        value = input("Type 'y' to continue calculating with {:.1f}, or type 'n' to start a "
                      "new calculation, or type 'c' to exit: ".format(result))
        if value == 'y':
            operand1 = result
        elif value == 'n':
            check = False
            calculator()
        else:
            check = False
            pass


calculator()
