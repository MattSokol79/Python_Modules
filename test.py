def list_of_multiples(num, length):
    list = []
    for i in range(1, (length + 1)):
        list.append(num * i)
    return list

print(list_of_multiples(7, 5))

