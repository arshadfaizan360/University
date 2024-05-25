def q1a(list1, list2):
    '''Returns a list that contains elements of two (non-empty) lists of integers, with duplicates removed, sorted in ascending order.'''
    # Combining the two lists
    combined_list = list1 + list2
    # Removing the duplicates
    unique_list = list(dict.fromkeys(combined_list))
    # Sorting the list
    sorted_list = unique_list.sort()
    return sorted_list

def q1b(numbers):
    '''Returns the median of integers in a non-empty list'''
    # Sorting the list
    sorted = numbers.sort()
    # Finding the median position
    pos = (len(sorted)+1)/2
    # Returning the median
    if int(pos) == pos:
        return sorted[pos-1]
    else:
        return (sorted[pos-1.5]+sorted[pos-0.5]) / 2

counties = "Dorset, Devon and Cornwall"
print(counties[8:13])

#########################################################

def calc_dist(i_vel, acc, time_s):
    '''Returns the distance travelled by a body, given its initial velocity and rate of acceleration'''
    return (i_vel * time_s) + time_s**2 * acc/2

i_vel = 10 #initial velocity
acc = 2 #acceleration
time_s = 10 #time in seconds

print(calc_dist(i_vel, acc, time_s))

assert time_s < 0, 'Time less than zero.'

def my_div (a, b):
       my_result = a / b
       return my_result

try:
    my_div(a, b)
except:
    print('Division Error')