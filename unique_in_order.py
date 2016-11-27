__author__ = 'Stan'


# Solution 1
def unique_in_order1(iterable):
    if len(iterable) <= 1:
        return list(iterable)
    items = list(iterable)
    result = []
    for i in range(0, len(items)):
        try:
            if items[i] != items[i+1]:
                result.append(items[i])
        except IndexError:
            result.append(items[i])
    return result


# Solution 2
def unique_in_order2(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result