import pandas as pd
import re

# Create the same FAQ data from Question 1.
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


def scoring_function(query, df):
    
    query_words = set(re.findall(r"\b\w+\b", query.lower()))

    results = []

    for index, row in df.iterrows():
        
        faq_text = f"{row['question']} {row['keywords']}".lower()
        faq_words = set(re.findall(r"\b\w+\b", faq_text))

        # The score is the number of words shared by the query and FAQ.
        score = len(query_words.intersection(faq_words))

        if score > 0:
            results.append({
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "confidence": score
            })

    
    results.sort(key=lambda x: x["confidence"], reverse=True)

    return pd.DataFrame(results)


query = input("Enter your question: ")

matches = scoring_function(query, df)

if matches.empty:
    print("\nNo matching FAQ entries found.")
else:
    print("\nMatching FAQ entries ranked by confidence:")
    print(matches.to_string(index=False))
