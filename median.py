"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        numbers.sort()
        length = len(numbers)
        if (length%2==0):
            lowerM = numbers[int((length/2)-1)]
            upperM = numbers[int(length/2)]
            median = (lowerM+upperM)/2

        else:
            median = numbers[int((length-1)/2)]
        break
print(median)
