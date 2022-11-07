# Count Palindromes
# GIven a list of strings, count the number of palindromes that occur inside of the list (a palindrome is a word that is spelled the same backwards and forward).

# Example input: [‘dog’, ‘racecar’, ‘wildebeest’]			
# Output: 1
# Explanation: ‘racecar’ is the only palindrome in the list

li = ["dog", "racecar", "wildebeest", "beeb", "dweeb", "mom"]

def whiteboard(arg):
    counter = 0
    for word in arg:
        if word == word[::-1]:
            counter += 1
    print(counter)

whiteboard(li)