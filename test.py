import math

def round_number(num):
    decimal = str(num).split('.')[1]
    # if the value after decimal is 5 or more it rounds up
    if decimal >= "5":
        math.ceil(num)
        return print(math.ceil(num))
    # else it rounds up
    else:
        math.floor(num)
        return print(math.floor(num))


while True:
    number = float(input("What number would you like to round?    "))
    print(str(number).split('.')[1])
    round_number(number)