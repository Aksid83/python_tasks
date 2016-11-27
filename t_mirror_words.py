"""
Question 2 - Mirror Words
Implement the procedure 'find_mirrors' found on the next page.
in_file contains a list of words, one word per line.
A sample list of words is available at: http://www.cs.duke.edu/~ola/ap/linuxwords
You will write to out_file a list of in_file words where the first word is a mirror image
(letter reversed) copy of the second word, and both words exist in in_file.
There should be one pair of words per line.
For example, out_file might contain: Bard/draB, Bud/duB, Are/erA, Bag/gaB, Brag/garB, etc.
Requirements:
Describe how your algorithm works
Describe why you chose to implement it the way you did.
Eliminate Palindrome words like eye, civic and deed
Use a case sensitive compare: Aa would match aA but not aa
Include a copy of out_file in your response
Just implement find_mirrors, we're not looking for other improvements
"""

import urllib

__author__ = 'Stan'


def mirror_words1(in_file, out_file):
    # Define the empty set for words from the input file.
    words = set()
    # Read each line from input file.
    for line in in_file:
        # Eliminating palindrome words: if current word is palindrome then skip it.
        if line.strip() == line.strip()[::-1]:
            continue
        # Check if current reversed word exists in words set.
        elif line.strip()[::-1] in words:
            # Reversed word is in set: then we found mirror word. Writing the line to the output file.
            out_file.write(line.strip() + '/' + line.strip()[::-1] + '\n')
            # Remove reversed word from the set to prevent duplicates.
            words.discard(line.strip()[::-1])
        # If reversed word is not in the set then add it to the set.
        else:
            words.add(line.strip())


# Sorting based on the word length
def mirror_words2(in_file, out_file):
    words = []
    mapper = {}
    # Creating array of the words from the file
    for line in in_file:
        if line.strip() != line.strip()[::-1]:
            words.append(line.strip())
    max_word = max(len(w) for w in words)
    for i in range(max_word + 1):
        mapper[i] = []
        for w in words:
            if len(w) == i:
                mapper[i].append(w)
        if len(mapper[i]) == 0 or len(mapper[i]) == 1:
            mapper.pop(i, None)
    for value in mapper.values():
        for i in range(len(value)-1):
            for j in range(i+1, len(value)):
                if value[i][::-1] == value[j]:
                    out_file.write(line.strip() + '/' + line.strip()[::-1] + '\n')


# Brute force. The slowest.
def mirror_words3(in_file, out_file):
    words = []
    for line in in_file:
        if line.strip() == line.strip()[::-1]:
            continue
        words.append(line.strip())
    print 'Total words: ', len(words)
    # Creating the first FOR loop for looping through words array using indexes.
    for i in range(len(words)-1):
        # Eliminating palindrome words: if current word is palindrome then skip it.
        if words[i] == words[i][::-1]:
            continue
        # The second FOR loop starts with the next index from the first loop
        for j in range(i+1, len(words)):
            # If the second word has different length then skip it.
            if len(words[i]) != len(words[j]):
                continue
            # Comparing the first reversed word with the second: if equal then we found mirror words.
            if words[i][::-1] == words[j]:
                print 'Mirror words: ', words[i] + '/' + words[j]
                out_file.write(line.strip() + '/' + line.strip()[::-1] + '\n')


linuxwords = urllib.urlopen('http://users.cs.duke.edu/~ola/ap/linuxwords').read()
output = open('linuxwords', 'w')
output.write(linuxwords)
output.close()
with open('linuxwords', 'r') as in_file:
    with open('output.txt', 'w') as out_file:
        mirror_words1(in_file, out_file)
        out_file.close()