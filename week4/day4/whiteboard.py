# Find Middle Number
# Given a number (n) and an array of numbers (num_list) as input to a function, return True if the number is greater than the middle number of the array. Return False if the number is less than the middle number of the array.
# Example Input: n = 6, array = [3,5,8, 10]			
# Example Output: True
# Example Input: n = 105, array = [10,30,44,22,100]
# Example Output: True

array = [3,5,8, 10]
n = 6

def whiteboard(li, n):
    length = len(li)

    if length % 2:
        middle = li[length//2]    
    else:
        middle = li[(length//2)-1]
    
    return n > middle

print(whiteboard(array, n))