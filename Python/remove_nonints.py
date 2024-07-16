def remove_non_ints(nums):
    new_list = []
    for num in nums:
        if type(num) == int:
            new_list.append(num)
    
    return new_list

print(remove_non_ints(["200", 300, 2, False, "other string", 6])) # Expected Output: [300, 2, 6]
print(remove_non_ints([True, 300, 2, False, "other string", 76, 86, "more strings"])) # Expected Output: [300, 2, 76, 86]
print(remove_non_ints([300, 300, 2, False, "other string", 6, {}, 16])) # Expected Output: [300, 300, 2, 6, 16]
print(remove_non_ints(["string", True, {}, []])) # Expected Output: []