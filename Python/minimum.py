def find_minimum(nums):
    min = nums[0]
    for num in nums:
        if num < min:
            min = num
    
    return min

print(find_minimum([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7])) # Expected Output: -4
print(find_minimum([4, 3, 2, 1, 18, 1, 2, 3, 4, 5, 6, 7])) # Expected Output: 1
print(find_minimum([43, 234, 65465, 234, 2343, 443, 2123, 8768])) # Expected Output: 43
print(find_minimum([0])) # Expected Output: 0