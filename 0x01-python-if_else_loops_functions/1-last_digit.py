#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
one = " and is greater than 5"
two = " and is 0"
three = " and is less than 6 and not 0"
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
if last_digit > 5:
    print("Last_digit digit of {} is {}".format(number, last_digit) + one)
elif last_digit == 0:
    print("Last_digit digit of {} is {}".format(number, last_digit) + two)
else:
    print("Last_digit digit of {} is {}".format(number, last_digit) + three)
