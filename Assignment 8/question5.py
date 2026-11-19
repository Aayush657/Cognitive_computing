from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Three short product reviews
reviews = [
    "These headphones have excellent sound quality and deep bass. "
    "The battery lasts all day, and the fit is very comfortable.",

    "I love these headphones because they sound amazing. "
    "The delivery was fast, and the product is worth buying.",

    "The headphones feel cheap and the sound keeps cutting out. "
    "The battery life is poor, and customer support was unhelpful.",

    "The headphones connect using Bluetooth and include a charging cable. "
    "They have adjustable ear cups and three control buttons."
]

positive_reviews = []

# 1 and 2. Find polarity, subjectivity, and classify reviews
for i, review in enumerate(reviews, start=1):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity

    if polarity > 0.1:
        sentiment = "Positive"
        positive_reviews.append(review)
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"\nReview {i}: {review}")
    print(f"Polarity: {polarity:.3f}")
    print(f"Subjectivity: {subjectivity:.3f}")
    print(f"Classification: {sentiment}")

# 3. Generate a word cloud from positive reviews
if positive_reviews:
    positive_text = " ".join(positive_reviews)

    wordcloud = WordCloud(
        width=1000,
        height=500,
        background_color='white',
        stopwords=STOPWORDS,
        collocations=False
    ).generate(positive_text)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of Positive Product Reviews")
    plt.show()
else:
    print("No positive reviews were found for the word cloud.")
