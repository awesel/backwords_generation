import random
import variable
wordvecs = variable.word_vecs

# read in adjective and noun lists
with open("adjectives.txt", "r") as adj_file:
    adjectives = adj_file.read().splitlines()
with open("nouns.txt", "r") as noun_file:
    nouns = noun_file.read().splitlines()

# generate list of all possible adjective-noun combinations
all_phrases = [noun1 + " " + noun2 for noun1 in nouns for noun2 in nouns 
               if noun1 in wordvecs and noun2 in wordvecs]

# randomly select 200 unique phrases
selected_phrases = random.sample(all_phrases, 10)

# write selected phrases to output file
with open("phrases.txt", "w") as output_file:
    for phrase in selected_phrases:
        output_file.write(phrase + "\n")
