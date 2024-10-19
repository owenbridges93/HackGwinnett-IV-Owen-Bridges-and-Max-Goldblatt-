#This code determines what words are incorrectly spelled in a sentence using an index of english words.



#The following code formats words.txt into a python set
dictionary = {}

with open("words.txt") as f:
    lines = f.readlines()    
    
num_lines = len(lines)

for i in range(num_lines):
    value = lines[i][0:-1]
    dictionary[i] = value

#Converts the dictionary dictionary into a set
dictionary = {dictionary[sub] for sub in dictionary}
#Converts all elements in dictionary to lower case
dictionary = {word.lower() for word in dictionary}

# Gets sample sentence from user
sentence = input("What is your sentence? ")
#This splits the sentence variable into a list, words.
words = sentence.split() 
#The following is for logging, is not used in the final code.
#print("Words in your sentence:", words)

#The spellcheck function compares the words list to the dictionary set.
def spell_check(words, dictionary):
    # Normalize words to lowercase to handle case sensitivity
    normalized_words = {word.lower().strip('.,!?:;()/@#$%^&*-=+1234567890') for word in words}
    
    # This finds incorrect words, correct words, and splits them into two different lists.
    correct_words = normalized_words & dictionary
    incorrect_words = normalized_words - dictionary
    incorrect_words_list = list(incorrect_words)

    #This stores the word placement of the incorrect words in the original sentence inputted by the user.
    incorrect_words_indices = []

    #This function determines the word placement of the incorrect words in the original sentence inputted by the user.
    for incorrect_word in range(len(incorrect_words)):
        i = 0
        for current_word in normalized_words:
            i+=1
            if incorrect_words_list[incorrect_word] == current_word:
                incorrect_words_indices.append(i)

    
    #Output
    print("Incorrect words:", incorrect_words)
    print("Incorrect words indices: ", incorrect_words_indices)
    print("Correct words:", correct_words)

spell_check(words, dictionary)
