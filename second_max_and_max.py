def second_max(array):
    max1, max2 = float('-inf'), float('-inf')
    for i in array:
        if i > max2:
            if i >= max1:
                max1, max2 = i, max1
            else:
                max2 = i
    print 'First maximum:', max1
    print 'Second maximum:', max2

array1 = [0]

second_max(array1)
