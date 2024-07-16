def area_sum(rectangles):
    sum = 0
    for rectangle in rectangles:
        area = rectangle['height'] * rectangle['width']
        sum += area
    return sum

print(area_sum([{"height": 4, "width": 5}])) # Expected Output: 20
print(area_sum([{"height": 2, "width": 3}, {"height": 4, "width": 5}])) # Expected Output: 26
print(area_sum([{"height": 10, "width": 11}, {"height": 12, "width": 13}])) # Expected Output: 266
print(area_sum([])) # Expected Output: 0