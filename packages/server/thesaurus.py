from nltk.corpus import wordnet as wn

def thesaurus(root):
    words = []
    for synonym in wn.synsets(root):
        for item in synonym.lemmas():
            words.append(item.name())
    return words