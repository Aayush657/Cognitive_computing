import pandas as pd

# Create the FAQ data used in the previous questions.
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


def same_category(category_name, df):
    # Select all FAQ entries that belong to the given category.
    return df[df["category"].str.lower() == category_name.lower()]


# My first personalized entry is in the account category.
category_name = "account"

print("FAQs belonging to the", category_name, "category:")
print(same_category(category_name, df).to_string(index=False))
