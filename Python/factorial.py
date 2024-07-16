def factorial(num):
    counter = 1
    fact = 1
    if num == 0:
        return 1
    while (counter <= num):
        fact *= counter
        counter += 1

    return fact

print(factorial(1)) # Expected Output: 1
print(factorial(5)) # Expected Output: 120
print(factorial(7)) # Expected Output: 5040
print(factorial(9)) # Expected Output: 362880
print(factorial(13)) # Expected Output: 6227020800