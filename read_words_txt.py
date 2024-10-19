wordlist = {}

with open("words.txt") as f:
    lines = f.readlines()    
    
num_lines = len(lines)

for i in range(num_lines):
    value = lines[i][0:-1]
    wordlist[i] = value

wordlist = {wordlist[sub] for sub in wordlist}
wordlist = {word.lower() for word in wordlist}

# Get user input
sentence = input("What is your sentence? ")
words = sentence.split() 
print("Words in your sentence:", words)

# List of incorrect words // replace with dictionary when possible
dictionary = wordlist  # Corrected this line

def spell_check(words, dictionary):
    # Normalize words to lowercase to handle case sensitivity
    normalized_words = {word.lower().strip('.,!?:;()/@#$%^&*-=+1234567890') for word in words}
    
    # Find correct and incorrect words
    correct_words = normalized_words & dictionary
    incorrect_words = normalized_words - dictionary
    incorrect_words_list = list(incorrect_words)

    incorrect_words_indices = []

    for incorrect_word in range(len(incorrect_words)):
        i = 0
        for current_word in normalized_words:
            i+=1
            if incorrect_words_list[incorrect_word] == current_word:
                incorrect_words_indices.append(i)

    print("Incorrect words:", incorrect_words)
    print("Incorrect words indices: ", incorrect_words_indices)
    print("Correct words:", correct_words)

spell_check(words, dictionary)
