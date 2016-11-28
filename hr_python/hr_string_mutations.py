"""
Read a given string, change the character at a given index and then print the modified string.

Input Format:
The first line contains a string, S.
The next line contains an integer i, denoting the index location and a character c separated by a space.

Output Format:
Using any of the methods explained above, replace the character at index i with character c.

Sample Input:
abracadabra
5 k

Sample Output:
abrackdabra
"""

s = raw_input()
i, c = raw_input().split()
i = int(i)

print s[:i] + c + s[i+1:]
