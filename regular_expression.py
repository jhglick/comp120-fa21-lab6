# File: regular_expression.py
# Author: COMP 120 class
# Date: October 12, 2021
# Description: Contains a regular expression example.

import re

if __name__ == "__main__":
    
    # Define the regular expression.
    # The regular expression should match all strings that alternate
    # a digit and a letter.  Strings can start with a digit or a letter,
    # and can end with a digit or a letter.
    reg_ex = ""  # fill in with a correct regular expression
    pattern = re.compile(reg_ex)

    # Test the regular expression
    num_tests = 0
    num_correct = 0

    s = "0a9B3z"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()

    s = "7"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()
    
    s = "7T"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()


    s = "7T2"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()

    s = "7T2R1"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()

    s = "0a9B3z"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()
    
    s = "7T"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()


    s = "7T2"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()

    s = "7T2R1"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()

    s = "a0B9z3"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()

    s = "t"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()
    
    s = "T7"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()


    s = "T7f"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()

    s = "T7R2V"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()

    s = "a0B9z3"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()
    
    s = "T7"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()


    s = "T7P"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()

    s = "T7R2w"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if ans:
        print(f"{s} matches your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} doesn't match your pattern.  Incorrect")
    print()

    s = ""
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if not ans:
        print(f"{s} doesn't match your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} matches your pattern.  Incorrect")
    print()

    s = "98"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if not ans:
        print(f"{s} doesn't match your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} matches your pattern.  Incorrect")
    print()

    s = "Fx"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if not ans:
        print(f"{s} doesn't match your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} matches your pattern.  Incorrect")
    print()

    s = "3t4St2H"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if not ans:
        print(f"{s} doesn't match your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} matches your pattern.  Incorrect")
    print()

    s = "3 t 3 J"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if not ans:
        print(f"{s} doesn't match your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} matches your pattern.  Incorrect")
    print()

    s = "3_t_3_J"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if not ans:
        print(f"{s} doesn't match your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} matches your pattern.  Incorrect")
    print()

    s = "3R2xm"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if not ans:
        print(f"{s} doesn't match your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} matches your pattern.  Incorrect")
    print()

    s = "R2H11"
    num_tests += 1
    print(f"Checking '{s}'")
    ans = re.fullmatch(pattern, s)
    if not ans:
        print(f"{s} doesn't match your pattern.  Correct")
        num_correct += 1
    else:
        print(f"{s} matches your pattern.  Incorrect")
    print()

    if num_tests == num_correct:
        print("All correct.  Nice job")
    else:
        print(f"Num tests = {num_tests}")
        print(f"Num correct = {num_correct}")
        print("Some incorrect.  Scroll back to see which ones.")


