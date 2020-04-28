#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if number < 0:
    last = number % -10
else:
    last = number % 10
string = "last digit of {} is {} and is {}"
if last > 5:
    print(string .format(n, last, "greater than 5"))
elif last == 0:
    print(string .format(n, last, "0"))
else:
    print(string .format(n, last, "less than 6 and not 0"))

