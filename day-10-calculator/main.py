from art import logo
from replit import clear

# def calculator(first_num, second_num, operator):
#     if operator == "+":
#         return first_num + second_num
#     if operator == "-":
#         return first_num - second_num
#     if operator == "*":
#         return first_num * second_num
#     if operator == "/":
#         return first_num / second_num
def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def final_cal():
    print(logo)
    first_num = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    continue_flag = True

    while continue_flag:
        operator = input("Pick an operation: ")
        next_num = float(input("What's the next number?: "))
        # result = calculator(first_num, next_num, operator)
        result = operations[operator](first_num, next_num)
        print(f"{first_num} {operator} {next_num} = {result}")
        decision = input(
            f"Type 'y' to coninue calculating with {result}, or type 'n' to start a new calculation: "
        ).lower()
        if decision == "y":
            first_num = result
        else:  #clear the screen and restart final_cal()
            continue_flag = False
            clear()
            final_cal()

final_cal()
