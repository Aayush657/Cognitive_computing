import pandas as pd

# My college roll number
roll_number = 1024170416

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

# Pick the first FAQ entry and ask the user for a new keyword.
entry_index = 0

print("Selected FAQ entry:")
print(df.loc[entry_index].to_string())

new_keyword = input("\nEnter a new keyword to add: ").strip()

if new_keyword:
    # Add the new keyword to the existing keywords.
    df.loc[entry_index, "keywords"] += " " + new_keyword

    # Save the complete updated DataFrame as a CSV file.
    filename = f"{roll_number}_faq_data.csv"
    df.to_csv(filename, index=False)

    print("\nUpdated FAQ entry:")
    print(df.loc[entry_index].to_string())

    print(f"\nUpdated DataFrame saved to {filename}")
else:
    print("No keyword was entered.")
