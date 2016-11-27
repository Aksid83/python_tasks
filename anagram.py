__author__ = 'Stan'


def normalize_string(string):
    """
    Removes spaces from the input string, makes all characters lower case.
    :param string: Any input string
    :return: Normalized string
    """
    return string.lower().replace(' ', '')


def count_letters(string):
    count = {}
    for letter in string:
        count[letter] = count.get(letter, 0) + 1
    return count


def find_anagram1(str1, str2):
    str1 = normalize_string(str1)
    str2 = normalize_string(str2)
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)
    

def find_anagram2(str1, str2):
    str1 = normalize_string(str1)
    str2 = normalize_string(str2)
    return count_letters(str1) == count_letters(str2)


print find_anagram1('aaaBBBc ccDDD', 'AAA d d d CCb cBb ')
print find_anagram2('aaaBBBccc DDD', 'AAA d d d CCb cBb ')


