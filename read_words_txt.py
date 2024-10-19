wordlist = {}

with open("words.txt") as f:
    lines = f.readlines()    
    
num_lines = len(lines)

for i in range(num_lines):
    value = lines[i][0:-1]
    wordlist[i] = value
