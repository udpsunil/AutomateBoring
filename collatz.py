def even(number):
    return not number%2


def collatz(number):
    if even(number):
        print(number // 2)
        return number // 2
    else:
        print(number * 3 + 1)
        return number * 3 + 1

number = int(input("Enter a number:"))

while (True):
    number = collatz(number)
    if number == 1:
        break
