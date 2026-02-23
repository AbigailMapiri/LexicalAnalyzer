import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.tag import UnigramTagger, DefaultTagger
from nltk.chunk import RegexpParser

# -------------------------------
# DOWNLOAD NLTK PACKAGES
# -------------------------------
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# -------------------------------
# LEXICONS
# -------------------------------

# CC1 - CC12
CC = {
    "CC1": {"yo"},
    "CC2": {"o"},
    "CC3": {"ba"},
    "CC4": {"o"},
    "CC5": {"le"},
    "CC6": {"a"},
    "CC7": {"se"},
    "CC8": {"tse"},
    "CC9": {"di"},
    "CC10": {"lo"},
    "CC11": {"mo"},
    "CC12": {"go"}
}

# L01 - L03 (Ink)
L = {
    "L01": {"sa"},
    "L02": {"tla"},
    "L03": {"nang"}
}

# Vnge (past relative verbs)
Vnge = {"tsamaeng", "ganeng", "nkutlweng", "direng"}

# Vng (present relative verbs)
Vng = {"tsamayang", "ganang", "nkutlwang", "dirang"}

# Pronouns
Pro = {"ene", "bone", "tsone", "yone"}

# Nouns
Nouns = {"dikgomo", "dinku", "motse", "ntlu", "madi"}

# Combine all lexicons
lexicons = {**CC, **L, "Vnge": Vnge, "Vng": Vng, "Pro": Pro, "Nouns": Nouns}

# -------------------------------
# TRAIN TAGGER
# -------------------------------
train_data = []
for words, tag in [(CC, "cc"), (Vnge, "Vnge"), (Vng, "Vng"), (Nouns, "Nouns"), (Pro, "Pro"), (L, "Ink")]:
    for key, word_set in (words.items() if isinstance(words, dict) else {w:w for w in words}.items()):
        for word in word_set:
            train_data.append((word, tag))

default_tagger = DefaultTagger("UNK")
tagger = UnigramTagger([train_data], backoff=default_tagger)

# -------------------------------
# ORIGINAL STRUCTURES
# -------------------------------
structures = [
    ["CC1","CC2","L02","Vng"],
    ["CC3","CC3","L02","Vng"],
    ["CC4","CC4","L02","Vng"],
    ["CC5","CC5","L02","Vng"],
    ["CC6","CC6","L02","Vng"],
    ["CC7","CC7","L02","Vng"],
    ["CC8","CC9","L02","Vng"],
    ["CC10","CC11","L02","Vng"],
    ["CC11","CC12","L02","Vng"],
    ["CC1","CC2","L01","Vnge"],
    ["CC3","CC3","L01","Vnge"],
    ["CC4","CC4","L01","Vnge"],
    ["CC5","CC5","L01","Vnge"],
    ["CC6","CC6","L01","Vnge"],
    ["CC7","CC7","L01","Vnge"],
    ["CC8","CC9","L01","Vnge"],
    ["CC10","CC11","L01","Vnge"],
    ["CC11","CC12","L01","Vnge"],
    ["CC1","CC2","L03","CC5","Nouns"],
    ["CC3","CC3","L03","CC5","Nouns"],
    ["CC4","CC4","L03","CC5","Nouns"],
    ["CC5","CC5","L03","CC5","Nouns"],
    ["CC6","CC6","L03","CC5","Nouns"],
    ["CC7","CC7","L03","CC5","Nouns"],
    ["CC8","CC9","L03","CC5","Nouns"],
    ["CC10","CC11","L03","CC5","Nouns"],
    ["CC11","CC12","L03","CC5","Nouns"]
]

# -------------------------------
# FUNCTION TO GENERATE SENTENCES
# -------------------------------
def generate_sentence(structure):
    words = []
    for tag in structure:
        if tag in lexicons:
            words.append(random.choice(list(lexicons[tag])))
        else:
            words.append(tag)
    return " ".join(words)

# -------------------------------
# GENERATE ONE EXAMPLE SENTENCE
# -------------------------------
sentence = generate_sentence(random.choice(structures))
print("Generated Sentence:")
print(sentence)

# -------------------------------
# TAGGING
# -------------------------------
tokens = word_tokenize(sentence)
tagged = tagger.tag(tokens)
print("\nTagged Sentence:")
print(tagged)

# -------------------------------
# CHUNKING WITH GRAMMAR
# -------------------------------
grammar = r"""
  NP: {<Nouns|Pro|Ink>+}
  VP: {<Vng|Vnge>+}
  CC: {<cc>+}
"""
chunk_parser = RegexpParser(grammar)
tree = chunk_parser.parse(tagged)
print("\nLeamanyi Detection:")
print(tree)

# -------------------------------
# GENERATE MULTIPLE SENTENCES
# -------------------------------
print("\nGenerated Sentences from All Structures:")
for struct in structures:
    print(generate_sentence(struct))