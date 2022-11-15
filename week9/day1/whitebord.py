# First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"

def whiteboard(str):
    for letter in range(len(str)):
        if str.count(str[letter]) == 1:
            return letter
    return -1

print(whiteboard("aabb"))