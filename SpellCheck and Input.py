# Get user input
sentence = input("What is your sentence? ")
words = sentence.split() 
print("Words in your sentence:", words)

# List of incorrect words // replace with dictionary when possible
dictionary = set(["owen", "stupid", "is", "very"])  # Corrected this line

def spell_check(words, dictionary):
    # Normalize words to lowercase to handle case sensitivity
    normalized_words = {word.lower().strip('.,!?') for word in words}
    
    # Find correct and incorrect words
    correct_words = normalized_words & dictionary
    incorrect_words = normalized_words - dictionary

    print("Incorrect words:", incorrect_words)
    print("Correct words:", correct_words)

spell_check(words, dictionary)