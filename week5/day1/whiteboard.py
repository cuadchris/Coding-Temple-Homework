# Reverse a String in a list
# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.
# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

list =  ["h","e","l","l","o"]

def whiteboard(li):
    left = 0
    right = len(li) - 1
    while left < right:
        li[left], li[right] = li[right], li[left]
        left += 1
        right -= 1
    return li

print(whiteboard(list))