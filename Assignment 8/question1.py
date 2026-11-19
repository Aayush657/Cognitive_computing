import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Download required NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

# Paragraph about my favourite topic: Cricket
paragraph = """
Cricket is my favorite sport because it combines strategy, patience, and teamwork.
I enjoy watching international matches, especially when skilled batters build partnerships under pressure.
Fast bowlers use pace and swing, while spinners trick batters with flight and turn.
A great captain studies the pitch, chooses smart field placements, and motivates every player.
The final overs are exciting because one boundary can change the result.
Cricket teaches discipline, resilience, and respect for opponents.
"""

# 1. Convert to lowercase and remove punctuation
lower_text = paragraph.lower()
clean_text = re.sub(r'[^\w\s]', '', lower_text)

print("Original Paragraph:")
print(paragraph)

print("\nLowercase Text:")
print(lower_text)

print("\nText after removing punctuation:")
print(clean_text)

# 2. Tokenize into sentences and words
sentences = sent_tokenize(paragraph)
words = word_tokenize(clean_text)

print("\nSentence Tokens:")
print(sentences)

print("\nWord Tokens:")
print(words)

# 3. Compare split() and word_tokenize()
split_tokens = lower_text.split()
nltk_tokens = word_tokenize(lower_text)

print("\nTokens using split():")
print(split_tokens)

print("\nTokens using word_tokenize():")
print(nltk_tokens)

print("\nDifference:")
print("split() separates text mainly using whitespace.")
print("word_tokenize() recognizes punctuation as separate tokens.")

# 4. Remove stopwords
stop_words = set(stopwords.words('english'))

filtered_words = [
    word for word in words
    if word not in stop_words and word.isalpha()
]

print("\nWords after removing stopwords:")
print(filtered_words)

# 5. Display word frequency distribution
frequency = FreqDist(filtered_words)

print("\nWord Frequency Distribution:")
for word, count in frequency.most_common():
    print(f"{word}: {count}")
