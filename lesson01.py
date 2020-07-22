def assertion(num):
    if isinstance(num, int):
        if num % 2 == 1:
            print("%d is odd" % num)
        else:
            print("%d is even" % num)
    else:
        print("Invalid number!")


def add(numbers_to_add):
    sum_of_numbers = 0
    for i in numbers_to_add:
        sum_of_numbers = sum_of_numbers + i
    return sum_of_numbers


def change(n):
    print("10:", n)
    print("2:", bin(n))
    print("8:", oct(n))
    print("16:", hex(n))


numbers = range(1, 101)
print("Total is {}".format(add(numbers)))
number = input("Please enter a number:")
assertion(number)
change(number)