from nltk.corpus import wordnet

# Function to get definitions of a word
def get_definitions(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        return "No definitions found for the word '{}'.".format(word)

    definitions = []
    for synset in synsets:
        definitions.append(synset.definition())

    return definitions

# Function to get synonyms of a word
def get_synonyms(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        return "No synonyms found for the word '{}'.".format(word)

    synonyms = []
    for synset in synsets:
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())

    return synonyms

# Function to get antonyms of a word
def get_antonyms(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        return "No antonyms found for the word '{}'.".format(word)

    antonyms = []
    for synset in synsets:
        for lemma in synset.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

    return antonyms

# Chatbot interaction loop
while True:
    user_input = input("Enter a word: ")

    # Get definitions, synonyms, and antonyms of the word
    definitions = get_definitions(user_input)
    synonyms = get_synonyms(user_input)
    antonyms = get_antonyms(user_input)

    print("Definitions:", definitions)
    print("Synonyms:", synonyms)
    print("Antonyms:", antonyms)
