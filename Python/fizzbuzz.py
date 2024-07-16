def fizz_buzz(start, end):
    while (start < end):
        if start % 3 == 0 and start % 5 == 0:
            print('fizzbuzz')
        elif start % 3 == 0:
            print('fizz')
        elif start % 5 == 0:
            print('buzz')
        else:
            print(start)
        
        start += 1

def main():
    test(1, 100)
    test(5, 30)
    test(1, 15)


def test(start, end):
    print("Starting test")
    fizz_buzz(start, end)
    print("======================")


main()