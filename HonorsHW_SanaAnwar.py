# Sana Anwar
# CS 100 H FALL 2023
# Honors Homework 1 

"""
Problem 1: Write a program that takes a list of integers and finds the length of the longest consecutive sequence. 
For example, given the list [100, 4, 200, 1, 3, 2], the program should output that the length of the longest consecutive sequence is 4, 
corresponding to the sequence [1, 2, 3, 4].

Problem 2: Write a program that takes a string containing only parentheses and checks if it is balanced. 
For example, for the input string (()()), the program should output that the parentheses are balanced. 
Conversely, for the string ((), it should indicate that the parentheses are not balanced.

Problem 3: Given a list of integers, write a program to find the second largest number in the list. 
If there is no second largest number (e.g., all numbers are the same), print a message indicating that. 
For example, given the list [10, 20, 20, 5, 5], the output should be “The second largest number is: 10”. 
If the input is [5, 5, 5], the program should output “There is no second largest number”.

Problem 4: Create two lists of integers and write a program that finds and prints the common elements between the two lists. 
For example, given the lists [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8], the program should output “The common elements are: [4, 5]”. 
If there are no common elements, such as with the lists [1, 2] and [3, 4], the output should indicate “There are no common elements”. 
"""

# Problem 1:
def long_sequence(nums):
    if not nums:
        return 0
    num_set = set(nums)
    long_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            long_streak = max(long_streak, current_streak)

    return long_streak

# Problem 2:
def balanced(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

# Problem 3:
def second_largest(nums):
    unique_nums = list(set(nums)) 
    if len(unique_nums) < 2:
        return "there is no second largest number"
    
    unique_nums.sort(reverse=True)  
    return "the second largest number is: " + str(unique_nums[1])

# Problem 4:
def find_common(list1, list2):
    common = set(list1).intersection(set(list2))
    
    if common:
        return "the common elements are: " + str(list(common))
    else:
        return "there are no common elements"
