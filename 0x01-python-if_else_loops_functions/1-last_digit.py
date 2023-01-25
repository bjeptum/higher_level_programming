#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
last_num = int(last_digit)
if number >= 0:
    if last_num < 6 and last_num != 0:
        print(f"Last digit of {number} is {last_num} and is \
than 6 but not 0")
    elif last_num == 0:
        print(f"Last digit of {number} is {last_num} and is 0")
    else:
        print(f"Last digit of {number} is {last_num} and is greater than 5")
elif number < 0:
    print(f"Last digit of {number} is {-last_num} and is less \
than 6 and not 0")
