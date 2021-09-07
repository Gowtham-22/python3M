# The variable sentence stores a string.
# Write code to determine how many words in sentence start and end with the same letter, including one-letter words.
# Store the result in the variable same_letter_count.


sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count=0
words=sentence.split()
for w in words:
  if w[0]==w[-1]:
    same_letter_count+=1
print(same_letter_count)
