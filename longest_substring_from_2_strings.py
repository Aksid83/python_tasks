"""
Given 2 strings.
Find the longest common substring.
"""


# Works only from the beginning
def lcs1(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    result = ''
    if len1 == 0 or len2 == 0:
        return result
    x, xs, y, ys = s1[0], s1[1:], s2[0], s2[1:]
    if x == y:
        result = x + lcs1(xs, ys)
    return result

# print lcs1('tesla', 'tltes')


def lcs2(s1, s2):
    length = 0
    result = ''
    for i in xrange(len(s1)):
        tmp_str = ''
        for j in xrange(len(s2)):
            tmp_len = 0
            while i + tmp_len < len(s1) and j + tmp_len < len(s2) and s1[i+tmp_len] == s2[j+tmp_len]:
                tmp_len += 1
                tmp_str += s1[i+tmp_len]
            if tmp_len > length:
                length = tmp_len
                result = tmp_str
    print length
    print result

lcs2('tesla', 'tltes')