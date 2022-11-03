# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

# def whiteboard(str1, str2):
#     print(str1.endswith(str2))

# whiteboard("fun", "u")

def whiteboard2(str1, str2):
    print(str1[-len(str2):] == str2)

whiteboard2("fun", "un")