def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculator():
    operator = input()
    first_number = int(input())
    second_number = int(input())
    result = 0

    if operator == "multiply":
        result = multiply(first_number, second_number)
    elif operator == "divide":
        result = divide(first_number, second_number)
    elif operator == "add":
        result = add(first_number, second_number)
    elif operator == "subtract":
        result = subtract(first_number, second_number)

    return result


print(int(calculator()))
