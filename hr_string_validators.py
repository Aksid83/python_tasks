"""
Python has built-in string validation methods for basic data.
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

Task:
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters,
alphabetical characters, digits, lowercase and uppercase characters.

Input Format:
A single line containing a string .

Output Format:
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

Sample Input:
qA2

Sample Output:
True
True
True
True
True
"""

# 1 version:
s = raw_input()

digit = False
alpha = False

for c in s:
    if c.isdigit():
        digit = True
    if c.isalpha():
        alpha = True
    if alpha and digit:
        break

print digit or alpha
print alpha
print digit
print alpha and ( s.islower() or not s.isupper() )
print alpha and ( s.isupper() or not s.islower() )


# 2 version:
s = raw_input()
print any(c.isalnum() for c in s)
print any(c.isalpha() for c in s)
print any(c.isdigit() for c in s)
print any(c.islower() for c in s)
print any(c.isupper() for c in s)
