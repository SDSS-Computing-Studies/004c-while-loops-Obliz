#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
Number=""
var=0

while var!=1:
    Number = float(input("please enter a number"))
    var=Number%2
    if var==0:
        print("That is an even integer, try again")
print("That is an odd number")