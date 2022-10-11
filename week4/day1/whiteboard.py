# Move Zeros
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example Input: [0,0,11,2,3,4]					
# Example Output: [11,2,3,4,0,0]

list = [0,0,11,2,3,4]

def whiteboard(list):
    counter = 0
    answer = []
    for i in list:
        if i != 0:
            answer.append(i)
        else:
            counter += 1
    answer.extend([0] * counter)
    return answer

print(whiteboard(list))