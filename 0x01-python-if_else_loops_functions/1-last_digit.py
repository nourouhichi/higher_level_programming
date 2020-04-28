#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if number < 0:
    last = n % -10
else:
    last = n % 10
string = "last digit of {} is {} and is {}"
if last > 5:
    print(string .format(number, last, 'greater than 5'))
elif last < 6 and last != 0:
    print(string .format(number, last, 'less than 6 and not 0'))
else:
    print(string .format(number, last, '0'))
