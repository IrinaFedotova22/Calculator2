import random
import math
res = 0
print('Welcome to calculator!')
operation = input("Enter your operation:")


def get_expression():
        first_num = int(input("Enter the 1st number:"))
        second_num = int(input("Enter your 2nd number:"))
        return first_num, second_num


def get_expression2():
        first_num = int(input("Enter the 1st number:"))
        return first_num


def addition(first_num, second_num):
    return first_num + second_num


def subtraction(first_num, second_num):
    return first_num - second_num


def division(first_num, second_num):
    if second_num != 0:
        return first_num / second_num
    else:
        print("This is an invalid input")


def multiplication(first_num, second_num):
    return first_num * second_num


def raising_to_the_power_of(first_num, second_num):
    return first_num ** second_num


def absolute_value(first_num):
    return abs(first_num)


def factorial(first_num):
    return math.factorial(first_num)


def arccos(first_num):
    return math.acos(first_num)


if operation == '+':
    first_num, second_num = get_expression()
    res = addition(first_num, second_num)
    print(res)
elif operation == '-':
    first_num, second_num = get_expression()
    res = subtraction(first_num, second_num)
    print(res)
elif operation == '/':
    first_num, second_num = get_expression()
    res = division(first_num, second_num)
    print(res)
elif operation == '*':
    first_num, second_num = get_expression()
    res = multiplication(first_num, second_num)
    print(res)
elif operation == '**':
    first_num, second_num = get_expression()
    res = raising_to_the_power_of(first_num, second_num)
    print(res)
elif operation == '||':
    first_num = get_expression2()
    res = abs(first_num)
    print(res)
elif operation == '!':
    first_num = get_expression2()
    res = math.factorial(int(first_num))
    print(res)
elif operation == 'arccos':
    first_num = get_expression2()
    res = math.acos(first_num)
    print(res)
elif operation == 'R':
    print(random.random())
else:
    print("This is an invalid input")
