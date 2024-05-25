def long_name(names):
    """Reads a non-empty list of names stored as strings and returns the first one with a length of more than 35 characters. 
    If none is found, then return the string ‘long name not found’."""
    # Iterating through names
    for name in names:
        # Checking if length is > 35
        if len(name) > 35:
            return name
    # When there are no long names
    return 'long name not found'

import math

def overall_mark(marks):
    '''Takes the first, second and third assessment marks as a list and returns the overall mark for the module.'''
    # Calculating the weighted marks
    weighted_marks = [0, 0, 0]
    weightings = [0.3, 0.3, 0.4]
    for x in range (3):
        weighted_marks[x] = math.ceil(marks[x] * weightings[x])
    # Returning overall mark
    return weighted_marks[0] + weighted_marks[1] + weighted_marks[2]

def add_3_nbrs(nbr1,nbr2,nbr3):
           var_c = -3
           nbr3 = 3
           return var_a + var_b + var_c
        
if __name__ == "__main__":
    var_a = 1
    var_b = 2
    var_c = 3
    print(add_3_nbrs(var_a, var_b, var_c))
    assert add_3_nbrs(var_a, var_b, var_c) == 0
    print(var_c)
    assert add_3_nbrs(var_a, var_b, var_c) == 6
