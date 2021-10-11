# File: permutations.py
# Author: COMP 120 class
# Date: October 12, 2021
# Description: Contains a function to return a list containing
# all permutations of a parameter list.  

def permutations(lst):
    """ 
    Return list containing all permutations of the list lst.
    """
    pass  # Replace this with your implementation of the function.

def permutations_recur(lst, i):
    """
    Returns a list all permutations of the list lst, 
    assuming indices 0, 1, ..., i - 1 are fixed
    already.
    """

    pass  # Replace this with your implementation of the function.


if __name__ == "__main__":
    # Test the code
    lst = ['a', 'b', 'c', 'd']
    correct_ans = [['a', 'b', 'c', 'd'], ['a', 'b', 'd', 'c'], 
            ['a', 'c', 'b', 'd'], ['a', 'c', 'd', 'b'], 
            ['a', 'd', 'b', 'c'], ['a', 'd', 'c', 'b'], 
            ['b', 'a', 'c', 'd'], ['b', 'a', 'd', 'c'], 
            ['b', 'c', 'a', 'd'], ['b', 'c', 'd', 'a'], 
            ['b', 'd', 'a', 'c'], ['b', 'd', 'c', 'a'], 
            ['c', 'a', 'b', 'd'], ['c', 'a', 'd', 'b'], 
            ['c', 'b', 'a', 'd'], ['c', 'b', 'd', 'a'], 
            ['c', 'd', 'a', 'b'], ['c', 'd', 'b', 'a'], 
            ['d', 'a', 'b', 'c'], ['d', 'a', 'c', 'b'], 
            ['d', 'b', 'a', 'c'], ['d', 'b', 'c', 'a'], 
            ['d', 'c', 'a', 'b'], ['d', 'c', 'b', 'a']]
    perms = permutations(lst)
    print("Your permutations: ")
    print(perms)
    print()
    print("Correct permutations: ")
    print(correct_ans)
    correct = True
    if len(perms) != len(correct_ans):
        correct = False
    else:
        for item in perms:
            if item not in correct_ans:
                correct = False
                break
    if correct:
        print("Correct.  Nice job")
    else:
        print("Not correct.  Keep working on it.")