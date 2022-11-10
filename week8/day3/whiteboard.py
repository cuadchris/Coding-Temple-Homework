# Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def whiteboard(li):
    res = {}
    for i in set(li):
        res[i] = li.count(i)
    print(list(res)[-1])

whiteboard([2,2,1,1,1,2,2])

def whiteboard2(li):
    print(max(set(li), key = li.count))

whiteboard2([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])