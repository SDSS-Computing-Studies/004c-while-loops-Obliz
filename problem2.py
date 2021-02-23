#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""
import random
import math
import time

targetNum = ""
guess = 4
count = 4
targetNum = input("What is your target Number?") 
targetNum = int(targetNum)

print("The target is " + str(targetNum))
print("===================")
while targetNum + 4 != guess:
    print(guess)
    guess = (guess + 4)
    count = count + 4