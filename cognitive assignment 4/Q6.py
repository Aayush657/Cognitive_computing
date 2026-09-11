import pandas as pd
import re

# Create the FAQ data.
faq_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    },
    {
        "question": "how do i update my registered mobile number",
        "answer": "Go to Settings > Account Details and update your registered mobile number.",
        "keywords": "mobile number update",
        "category": "account"
    },
    {
        "question": "how can i check my latest fee payment status",
        "answer": "You can check your latest fee payment status from the payments section of your account.",
        "keywords": "fee payment status",
        "category": "billing"
    }
]

df = pd.DataFrame(faq_entries)


def scoring_function_with_ties(query, df):
    # Break the query into individual words.
    query_words = set(re.findall(r"\b\w+\b", query.lower()))

    results = []

    for index, row in df.iterrows():
        # Check both the question and keywords for matching words.
        faq_text = f"{row['question']} {row['keywords']}".lower()
        faq_words = set(re.findall(r"\b\w+\b", faq_text))

        score = len(query_words.intersection(faq_words))

        if score > 0:
            results.append({
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "confidence": score
            })

    results.sort(key=lambda x: x["confidence"], reverse=True)

    if not results:
        print("No matching FAQ entries found.")
        return

    results_df = pd.DataFrame(results)
    highest_score = results_df["confidence"].max()

    # Show every entry if more than one has the highest score.
    best_matches = results_df[results_df["confidence"] == highest_score]

    print("\nHighest confidence score:", highest_score)

    if len(best_matches) > 1:
        print("Tie detected. All equally good matches are:")
    else:
        print("No tie. Best match is:")

    print(best_matches.to_string(index=False))


# This query produces a tie because both billing questions contain "fee".
print("Q6 - Query producing a tie:")
scoring_function_with_ties("fee", df)


# This query gives one clear best match.
print("\nQ6 - Query without a tie:")
scoring_function_with_ties("password reset", df)
