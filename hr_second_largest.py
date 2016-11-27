"""
You are given N numbers. Store them in a list and find the second largest number.
Input Format
The first line contains N. The second line contains an array A[] of N integers each separated by a space.
Output Format
Output the value of the second largest number.
Sample Input:
5
2 3 6 6 5
Sample Output: 5
"""

n = int(raw_input())
inp_arr = raw_input().split()
for i in inp_arr:
    i = int(i)
f_max = max(inp_arr)
while max(inp_arr) >= f_max:
    inp_arr.remove(f_max)
print max(inp_arr)