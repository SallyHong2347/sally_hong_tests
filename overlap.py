# Overview
# This program accepts two lines of input where each line contains the lower and upper bound of
# a line in 1D, and return a message about whether the lines intercepts

# functionality
# This program assumes user's input are floats and will raise exception if either 
# received invalid input or the value exceeds the maximum float representable by python

# issues
# This program can't handle arbitrarily large/small user input
# The program's precision is confined by the precision of float in python
# The program can only compare finite line segments


def overlap(line1, line2):
    x1, x2 = line1
    x3, x4 = line2
    # check bound validity
    if x1 > x2:
        x1, x2 = x2, x1
    if x3 > x4:
        x3, x4 = x4, x3
    
    # make x1, x2 the line with minimum lower bound
    if x1 > x3:
        x1, x3 = x3, x1
        x2, x4 = x4, x2
    
    # check overlap
    return not (x3 > x2)


try:
    line1 = input("Enter the lower and upper bounds of the first line separated by space: ").split()
    line2 = input("Enter the lower and upper bounds of the second line separated by space: ").split()
    
    # check input validity
    if len(line1) != 2 or len(line2) != 2:
        raise ValueError("please give two numbers for each line")

    # check overflow error
    for val in (*line1, *line2):
        if val == float('inf') or val == float('-inf'):
            raise OverflowError("unable to represent number")


    line1 = (float(line1[0]), float(line1[1]))
    line2 = (float(line2[0]), float(line2[1]))

    # Check if the lines overlap
    if overlap(line1, line2):
        print("The two lines overlap.")
    else:
        print("The two lines do not overlap.")
        
except ValueError as e:
    print(f"Invalid input: {e}")
except OverflowError as e:
    print(f"Overflow error: {e}")