def divide_list(nums, divisor):
    divided_nums = []
    for num in nums:
        divided_nums.append(num / divisor)
    return divided_nums

print(divide_list([100, 200, 300, 400], 10))
print(divide_list([27, 54, 81], 9))