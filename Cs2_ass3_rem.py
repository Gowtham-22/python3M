    
# 2. Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

from collections import Counter

str1 = "peter piper picked a peck of pickled peppers"
freq = Counter(str1)

for i in str1:
    print(i, freq[i])
    
# 3. Provided is a string saved to the variable name s1.
# Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.

s1 = "hello"

def char_frequency(s1):
    dict = {}
    for n in s1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

counts = char_frequency(s1)
print(counts)

# 4. Create a dictionary, freq_words, that displays each word in string str1 as the key and its frequency as the value.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

freq_words = word_count(str1)
print(freq_words)

# 5. Create a dictionary called wrd_d from the string sent,
# so that the key is a word and the value is how many times you have seen that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

wrd_d  = word_count(sent)
print(wrd_d)

# 6. Create the dictionary characters that shows each character from the string sally and its frequency.
# Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters = {}
for i in sally:
    characters[i]=characters.get(i,0)+1
    
sorted(characters.items(), key=lambda x: x[1])
best_char = sorted(characters.items(), key=lambda x: x[1])[-1][0]

# 7. Do the same as above but now find the least frequent letter.
# Create the dictionary characters that shows each character from string sally and its frequency.
# Then, find the least frequent letter in the string and assign the letter to the variable worst_char.

sally = "sally sells sea shells by the sea shore and by the road"

characters = {}
for i in sally:
    characters[i]=characters.get(i,0)+1
    
sorted(characters.items(), key=lambda x: x[1])
worst_char = sorted(characters.items(), key=lambda x: x[1])[-13][0]

# 9. Create a dictionary called low_d that keeps track of all the characters in the string p
# and notes how many times each character was seen. Make sure that there are no repeats of characters as keys,
# such that “T” and “t” are both seen as a “t” for example.

import collections
p = p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d  = collections.defaultdict(int)

for c in p:
    low_d[c] += 1
        
for c in sorted(low_d, key=low_d.get, reverse=True):
    if low_d[c] > 1:
        print('%s %d' % (c, low_d[c]))
