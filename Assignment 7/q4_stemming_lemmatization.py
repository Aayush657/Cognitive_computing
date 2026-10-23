# UCS420: Cognitive Computing - Assignment 7 (NLP-I)
# Q4. Stemming and lemmatization
# Roll number: 1024170416

import pandas as pd
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.stem import LancasterStemmer, PorterStemmer, RegexpStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from starter import df, process_ticket

unique_final = sorted({t for text in df["Ticket_Text"] for t in process_ticket(text)["final"]})

# POS tags are taken in context (each sentence is tagged as a whole) and stored against the
# lowercase form, which is how process_ticket() writes its tokens.
tag_of = {}
for text in df["Ticket_Text"]:
    for sentence in sent_tokenize(text):
        for word, tag in pos_tag(word_tokenize(sentence)):
            tag_of.setdefault(word.lower(), tag)


def wordnet_pos(tag):
    """Map a Penn Treebank tag (NN, VBD, JJ, RB, ...) to the WordNet POS the lemmatizer expects."""
    return {"J": wordnet.ADJ, "V": wordnet.VERB, "R": wordnet.ADV}.get(tag[0], wordnet.NOUN)


# Regexp suffix chosen from my own data: five final tokens end in the verb suffix "-ing"
# (syncing, restarting, responding, asking, running), more than any other suffix, so "ing$" is the
# rule that normalises the most words. min=6 leaves short words alone.
porter = PorterStemmer()
lancaster = LancasterStemmer()
regexp = RegexpStemmer("ing$", min=6)
lemmatizer = WordNetLemmatizer()

rows = []
for word in unique_final:
    tag = tag_of.get(word, "NN")
    outputs = {
        "Porter": porter.stem(word),
        "Lancaster": lancaster.stem(word),
        "Regexp(ing$)": regexp.stem(word),
        "WordNet+POS": lemmatizer.lemmatize(word, wordnet_pos(tag)),
    }
    if len(set(outputs.values())) > 1:  # keep only the words where the four methods disagree
        rows.append({"Word": word, "POS": tag, **outputs})

table = pd.DataFrame(rows)
print(f"Unique final tokens: {len(unique_final)}   Words where the outputs differ: {len(table)}\n")
print(table.to_string(index=False))

# Observe (starter notebook): Give one over-stemming and one under-stemming example from your table.
# Over-stemming (too much cut off, so unrelated words collapse together): Lancaster turns "portal" into
#   "port" and "campus" into "camp" - a student portal and a network/USB port would now look like the same
#   word. Lancaster's "several" -> "sev" and "student" -> "stud" are cut so far they are unrecognisable.
#   The Regexp rule turns "anything" into "anyth", because the "-ing" there is not a suffix at all.
# Under-stemming (related forms not merged): the Regexp rule turns "running" into "runn", so "running"
#   and "run" would still be different words (Porter and the lemmatizer both give "run"); it also leaves
#   "stopped" untouched, so it never meets "stop".
