# Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

def whiteboard(str):
    str1 = list(str)
    left = 0
    right = len(str) - 1
    while left < right:
        if str1[left] not in 'aeiou':
            left += 1
        elif str1[right] not in 'aeiou':
            right -= 1
        elif str1[left] and str1[right] in 'aeiou':
            str1[left], str1[right] = str1[right], str1[left]
            left += 1
            right -= 1
    print("".join(str1))

whiteboard("leetcode")