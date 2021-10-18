    
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
