# File: is_palindrome.py
# Author: COMP 120 class
# Date: October 12, 2021
# Description: Contains a recursive function to check if a string
# is a palindrome.

def is_palindrome(s):
    """
    Returns True if s is a palindrome, and False if not.
    """
    pass # you replace this with the correct function implementation.

if __name__ == "__main__":
    # Test the code

    s = "amanaplanacanalpanama"
    print(f"Checking '{s}'")
    ans = is_palindrome(s)
    print(f"Your function returned {ans}")
    if ans == True:
        print("Correct")
    else:
        print("Incorrect")
    print()

    s = "ablewasiereisawelba"
    print(f"Checking '{s}'")
    ans = is_palindrome(s)
    print(f"Your function returned {ans}")
    if ans == True:
        print("Correct")
    else:
        print("Incorrect")
    print()

    s = "ablewasiereisawelba"
    print(f"Checking '{s}'")
    ans = is_palindrome(s)
    print(f"Your function returned {ans}")
    if ans == True:
        print("Correct")
    else:
        print("Incorrect")
    print()

    s = "neveroddoreven"
    print(f"Checking '{s}'")
    ans = is_palindrome(s)
    print(f"Your function returned {ans}")
    if ans == True:
        print("Correct")
    else:
        print("Incorrect")
    print()

    s = ""
    print(f"Checking '{s}'")
    ans = is_palindrome(s)
    print(f"Your function returned {ans}")
    if ans == True:
        print("Correct")
    else:
        print("Incorrect")
    print()

    s = "a"
    print(f"Checking '{s}'")
    ans = is_palindrome(s)
    print(f"Your function returned {ans}")
    if ans == True:
        print("Correct")
    else:
        print("Incorrect")
    print()

    s = "aa"
    print(f"Checking '{s}'")
    ans = is_palindrome(s)
    print(f"Your function returned {ans}")
    if ans == True:
        print("Correct")
    else:
        print("Incorrect")
    print()

    s = "ab"
    print(f"Checking '{s}'")
    ans = is_palindrome(s)
    print(f"Your function returned {ans}")
    if ans == False:
        print("Correct")
    else:
        print("Incorrect")
    print()

    s = "aaadaa"
    print(f"Checking '{s}'")
    ans = is_palindrome(s)
    print(f"Your function returned {ans}")
    if ans == False:
        print("Correct")
    else:
        print("Incorrect")
    print()

    s = "aaaaadaa"
    print(f"Checking '{s}'")
    ans = is_palindrome(s)
    print(f"Your function returned {ans}")
    if ans == False:
        print("Correct")
    else:
        print("Incorrect")
    print()


    

