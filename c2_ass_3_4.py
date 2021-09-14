# 3. Assign to the variable num_lines the number of lines in the file school_prompt.txt.

num_lines = sum(1 for line in open('school_prompt.txt'))

# 4. Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

f = open('school_prompt.txt', 'r')
beginning_chars = f.read(30)
print(beginning_chars)
