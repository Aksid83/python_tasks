__author__ = 'Stan'


def binary_array_to_number1(arr):
    str_arr = []
    for el in arr:
        str_arr.append(str(el))
    return int(''.join(str_arr), 2)


def binary_array_to_number2(arr):
    return int(''.join(map(str, arr)), 2)


def binary_array_to_number3(arr):
    return int(''.join(str(a) for a in arr), 2)

print (binary_array_to_number1([0,0,0,1]))

