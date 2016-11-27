__author__ = 'Stan'


def reverse1(string):
    return string[::-1]


def reverse2(string):
    for i in range(len(string)-1, -1, -1):
        yield string[i]


def reverse3(string):
    return ''.join([string[i] for i in range(len(string)-1, -1, -1)])


def reverse4(string):
    if len(string) <= 1:
        return string
    return reverse4(string[1:]) + string[0]


def reverse5(string):
    result = ''
    index = len(string) - 1
    for i in range(len(string)):
        result += string[index]
        index -= 1
    return result

print reverse1('TestString123')
print ''.join(reverse2('TestString456'))
print reverse3('TestString789')
print reverse4('TestString987')
print reverse5('TestString555')
