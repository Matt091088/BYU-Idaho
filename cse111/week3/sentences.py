import random

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word


def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    verb = random.choice(verbs)
    return verb

def get_adjective():
    adjectives = ["nice", "white", "happy", "mad", "happy", "skinny", "fat", "beautiful", "ugly", "strong", "weak"]
    return random.choice(adjectives)

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"


def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = f"{determiner} {adjective} {noun} {verb} {prepositional_phrase}."
    return sentence.capitalize()


def main():
    sentence1 = make_sentence(1, "past")
    sentence2 = make_sentence(1, "present")
    sentence3 = make_sentence(1, "future")
    sentence4 = make_sentence(2, "past")
    sentence5 = make_sentence(2, "present")
    sentence6 = make_sentence(2, "future")

    print(sentence1)
    print(sentence2)
    print(sentence3)
    print(sentence4)
    print(sentence5)
    print(sentence6)

if __name__ == "__main__":
    main()
