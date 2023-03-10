import os
import variable
import requests
import random

wordvecs = variable.word_vecs

cool_modifiers = ["vintage polaroid", "4k image award winning photograph", "digital art", "painted by salvador dali", "pixel art", "pencil drawing", "cubist", "painted by picasso"]

def generate_phrases():
    with open("adjectives.txt", "r") as adj_file:
        adjectives = adj_file.read().splitlines()
    with open("nouns.txt", "r") as noun_file:
        nouns = noun_file.read().splitlines()

    # generate list of all possible adjective-noun combinations
    all_phrases = [noun1 + " " + noun2 + " " + modifier for noun1 in nouns for noun2 in nouns for modifier in cool_modifiers
                if noun1 in wordvecs and noun2 in wordvecs]

    # randomly select 200 unique phrases
    selected_phrases = random.sample(all_phrases, 10)
    

    # write selected phrases to output file
    with open("phrases.txt", "w") as output_file:
        for phrase in selected_phrases:
            output_file.write(phrase + "\n")



import openai

def get_first(input_string):
    return input_string.split()[0]

def get_second(input_string):
    return input_string.split()[1]
openai.api_key = "no api key for you"

def generate_file(image_url, prompt):
    response = requests.get(image_url)
    open(get_first(prompt) + "_" + get_second(prompt) + ".png", 'wb').write(response.content)





def generate_image(brompt):
    response = openai.Image.create(
        prompt=brompt,
        n=1,
        size="1024x1024",
        )
    print(response["data"][0]["url"])
    generate_file(response["data"][0]["url"], brompt)

def generate_from_text(filename):           
    with open(filename, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            PROMPT = line
            print (i)
            print (PROMPT)
            generate_image(PROMPT)
            distance_array_1 = generate_distances(get_first_word(PROMPT))
            distance_array_2 = generate_distances(get_second_word(PROMPT))

            order_array_1 = generate_order(distance_array_1)
            order_array_2 = generate_order(distance_array_2)

            to_text(order_array_1)
            to_text(order_array_2)






word_vecs = variable.word_vecs

def to_text(balls):
    file_name = f"{balls[0]}.txt"
    file_content = ""
    for i in range(len(balls)):
        file_content += f"{balls[i]}\n"

    with open(file_name, "w") as bile:
        bile.write(file_content)


def generate_order(distances):
    return sorted(distances.keys(), key=lambda x: distances[x])


def generate_distances(word):
    local_dict = {}
    for k in word_vecs:
        added = 0
        for j in range(300):
            distance = word_vecs[word][j] - word_vecs[k][j]
            added += distance * distance
        local_dict[k] = added**0.5
    return local_dict

def get_first_word(word):
    return word.split()[0]

def get_second_word(word):
    return word.split()[1]

generate_phrases()
generate_from_text("phrases.txt")
    
