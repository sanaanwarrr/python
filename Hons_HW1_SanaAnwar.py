# Problem 1
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

# Problem 1 Testing
nums = [100, 4, 200, 1, 3, 2]
print("the length of the longest consecutive sequence is:", long_sequence(nums))





# Problem 2
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

# Problem 2 Testing
s1 = "(()())"
s2 = "(()"
print("string", s1, "is balanced:", balanced(s1))
print("string", s2, "is balanced:", balanced(s2))





# Problem 3
def second_largest(nums):
    unique_nums = list(set(nums))  # Remove duplicates
    if len(unique_nums) < 2:
        return "there is no second largest number"
    
    unique_nums.sort(reverse=True)  # Sort in descending order
    return "the second largest number is: " + str(unique_nums[1])

# Problem 3 Testing
nums1 = [10, 20, 20, 5, 5]
nums2 = [5, 5, 5]
print(second_largest(nums1))
print(second_largest(nums2))





# Problem 4
def find_common(list1, list2):
    common = set(list1).intersection(set(list2))
    
    if common:
        return "the common elements are: " + str(list(common))
    else:
        return "there are no common elements"

# Problem 4 Example
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [1, 2]
list4 = [3, 4]
print(find_common(list1, list2))
print(find_common(list3, list4))