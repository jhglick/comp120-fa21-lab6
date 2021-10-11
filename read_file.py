"""
File: read_file.py 
Author: COMP 120 class
Date: October 12, 2021
Description: Program that reads a file.
"""

def read_file(filename):
    """ 
    Reads the file whose name is filename.
    Returns a list containing the average of the numbers
    on each line of the file.  If a line is empty or has a non-number on it,
    the line should be ignored and not included in the returned averages list.
    """
    pass  # Replace this with your implementation of the function.

if __name__ == "__main__":
    # Test program.
    file = "test.txt"
    print(f"Testing {file}")
    correct = [6498.2, 489.11, 4991.865750000001, 5108.165, 232.0]
    averages = read_file(file)
    print(f"Correct averages = {correct}")
    print(f"Your averages: {averages}")
    if correct == averages:
        print("Correct.  Nice job!")
    else:
        print("Incorrect.  Keep working on it.")
    print()

    file = "test2.txt"
    print(f"Testing {file}")
    correct = None
    averages = read_file(file)
    print(f"Correct averages = {correct}")
    print(f"Your averages: {averages}")
    if correct == averages:
        print("Correct.  Nice job!")
    else:
        print("Incorrect.  Keep working on it.")