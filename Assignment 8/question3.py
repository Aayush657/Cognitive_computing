import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Three cricket-related texts
texts = [
    "The batter played attacking cricket. The batter scored a century and helped the cricket team win.",
    "The bowler used swing bowling. The bowler took five wickets with accurate yorkers in the final overs.",
    "The captain led the team calmly. The captain chose smart field placements and motivated the cricket team."
]

# 1. Bag of Words using CountVectorizer
count_vectorizer = CountVectorizer(stop_words='english')
bow_matrix = count_vectorizer.fit_transform(texts)

print("Bag of Words Vocabulary:")
print(count_vectorizer.get_feature_names_out())

print("\nBag of Words Matrix:")
print(bow_matrix.toarray())

# 2. Calculate TF-IDF scores
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(texts)

feature_names = tfidf_vectorizer.get_feature_names_out()

print("\nTF-IDF Matrix:")
print(np.round(tfidf_matrix.toarray(), 3))

# 3. Display top 3 keywords for each text
print("\nTop 3 Keywords for Each Text:")

for i, row in enumerate(tfidf_matrix.toarray()):
    # Sort by descending TF-IDF score
    top_indices = sorted(
        range(len(feature_names)),
        key=lambda j: (-row[j], feature_names[j])
    )[:3]

    print(f"\nText {i + 1}:")
    for index in top_indices:
        print(f"{feature_names[index]}: {row[index]:.4f}")
