# 7. Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

f = open('travel_plans.txt', 'r')
first_chars = f.read(33)
print(first_chars)

# 8. Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

fileref = open('school_prompt.txt', 'r')
words = fileref.read().split()
p_words = [word for word in words if 'p' in word]
