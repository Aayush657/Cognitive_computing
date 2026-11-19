import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Two technology descriptions, each with 5 lines
ai_text = """
Artificial intelligence enables computers to learn from data.
AI systems recognize patterns and solve complex problems.
Machine learning improves predictions through training.
AI is used in healthcare, education, and automation.
Intelligent systems help people make faster decisions.
"""

blockchain_text = """
Blockchain stores data across a distributed network.
Blocks record transactions in a linked digital ledger.
Cryptography helps keep blockchain records secure.
Blockchain supports digital payments and smart contracts.
Network participants verify transactions without one central authority.
"""

# 1. Preprocess and tokenize both texts
tokens_ai = re.findall(r'[a-zA-Z]+', ai_text.lower())
tokens_blockchain = re.findall(r'[a-zA-Z]+', blockchain_text.lower())

clean_ai = " ".join(tokens_ai)
clean_blockchain = " ".join(tokens_blockchain)

print("AI Tokens:")
print(tokens_ai)

print("\nBlockchain Tokens:")
print(tokens_blockchain)

# 2a. Jaccard Similarity using sets
set_ai = set(tokens_ai)
set_blockchain = set(tokens_blockchain)

intersection = set_ai.intersection(set_blockchain)
union = set_ai.union(set_blockchain)

jaccard = len(intersection) / len(union) if union else 0

print("\nCommon Words:")
print(intersection)

print("\nJaccard Similarity:", round(jaccard, 4))

# 2b. Cosine Similarity using TF-IDF
texts = [clean_ai, clean_blockchain]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

cosine = cosine_similarity(
    tfidf_matrix[0:1],
    tfidf_matrix[1:2]
)[0][0]

print("Cosine Similarity:", round(cosine, 4))

# 2c. Compare the metrics
print("\nAnalysis:")
print("Jaccard measures the overlap between unique words.")
print("Cosine similarity compares TF-IDF-weighted text vectors.")

if jaccard < 0.2 and cosine < 0.2:
    print("Both metrics indicate low word-based similarity.")
else:
    print("The metrics show some degree of word-based similarity.")

print(
    "For these descriptions, cosine similarity can provide more "
    "information about term importance, while Jaccard gives a "
    "simple comparison of shared vocabulary."
)
