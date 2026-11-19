import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required resources
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

# Same paragraph as Q1
paragraph = """
Cricket is my favorite sport because it combines strategy, patience, and teamwork.
I enjoy watching international matches, especially when skilled batters build partnerships under pressure.
Fast bowlers use pace and swing, while spinners trick batters with flight and turn.
A great captain studies the pitch, chooses smart field placements, and motivates every player.
The final overs are exciting because one boundary can change the result.
Cricket teaches discipline, resilience, and respect for opponents.
"""

# 1. Extract alphabetic words using regular expressions
words = re.findall(r'[a-zA-Z]+', paragraph.lower())

print("Alphabetic Words:")
print(words)

# 2. Remove stopwords
stop_words = set(stopwords.words('english'))

filtered_words = [
    word for word in words
    if word not in stop_words
]

print("\nWords after Removing Stopwords:")
print(filtered_words)

# 3. Perform stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

print("\nStemmed Words:")
print(stemmed_words)

# 4. Perform lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [
    lemmatizer.lemmatize(word) for word in filtered_words
]

print("\nLemmatized Words:")
print(lemmatized_words)

# 5. Compare the outputs
print("\nComparison:")
for original, stem, lemma in zip(
    filtered_words, stemmed_words, lemmatized_words
):
    print(f"{original:15} Stem: {stem:12} Lemma: {lemma}")
