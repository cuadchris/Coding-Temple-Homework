# Find Palindrome
# Given a string of lowercase letters, write a function to see if the word is a palindrome (the same word spelled forward and backwards).		
# Example Input: ‘racecar’
# Example Output: True

def palinDrome(string):
    return string == string[::-1]


print(palinDrome("hello"))
print(palinDrome("doodle"))
print(palinDrome("racecar"))
print(palinDrome("refer"))