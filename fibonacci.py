__author__ = 'Stan'


def fib1(n):
    result = []
    a, b = 0, 1
    result.insert(a, a)
    while b < n:
        result.append(b)
        a, b = b, a + b

    return result


def fib2(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return a


def fib3(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib3(n-1) + fib3(n-2)


print 'F1: ', fib1(10)

print 'F2: ', fib2(10)

print 'F3: ', fib3(5)