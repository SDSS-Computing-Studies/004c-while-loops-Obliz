#!python3
"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""
import random
import math
import time

targetNum = 20
guess = 2
count = 2

print("The target is " + str(targetNum))
print("===================")
while targetNum + 2 != guess:
    print(guess)
    guess = (guess + 2)
    count = count + 2