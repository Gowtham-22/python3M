# 5. Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

three = []

with open('school_prompt.txt', 'r') as f:
    three = [line.split()[2] for line in f]
    print(three)

# 6. Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

fileref = open ("emotion_words.txt","r")
line = fileref.readlines()
emotions = []
for words in line:
    word = words.split()
    emotions.append(word[0])
print (emotions)
