#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = abs(number) % 10
if number < 0:
   l_digit = -l_digit
print("Last digit of {} is {} and is ".format(number, l_digit), end="")
if l_digit > 5:
    print("greater than 5")
elif l_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
