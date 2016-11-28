"""
Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:
Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Sample Designs:

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format:
A single line containing the space separated values of N and M.

Output Format:
Output the design pattern.

Sample Input:
9 27

Sample Output:

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

Note:
More than 6 lines of code will result in a score of 0.
Comment lines are counted. Blank lines are not counted.
"""

N, M = map(int, raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in xrange(1, N, 2):
    print (i * ".|.").center(M, "-")
print "WELCOME".center(M, "-")
for i in xrange(N-2, -1, -2):
    print (i * ".|.").center(M, "-")
