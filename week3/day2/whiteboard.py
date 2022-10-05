# Consecutive Indices
# You are given a list of unique integers (arr), and two integers (a and b). Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).
# It is guaranteed that a and b are both present in arr.
# Example:
# Input: ([1, 6, 9, -3, 4, -78, 0], -3, 4)				
# Output: True
# Input: ([3,1,0,19], 19, 0)	
# Output: True


list = [1, 6, 9, -3, 4, -78, 0]
num1 = -3
num2 = 4


def whiteboard2(l1, n1, n2):
    return l1.index(n1) == l1.index(n2) - 1
    
print(whiteboard2(list, num1, num2))




def whiteboard(l1, n1, n2):
    for x,y in enumerate(l1):
        if x+1 < len(l1):
            if l1[x] == n1 and l1[x+1] == n2:
                return True

    return False
    
print(whiteboard(list, num1, num2))