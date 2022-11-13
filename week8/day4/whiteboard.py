# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# rn = 'aabbfte'
# mag = 'tteebbbbbaaa'

rn = 'aabbfte'
mag = 'tt  f    eebbbbbaaa'

def whiteboard(ransom, magazine):
    res = []
    for letter in ransom:
        if letter in magazine:
            res.append(magazine.count(letter) >= ransom.count(letter))
        else:
            return False
    if res == []:
        return False
    return all(res)

print(whiteboard(rn, mag))