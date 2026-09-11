import pandas as pd

# My roll number
roll_number = 1024170416

# The last two digits are 1 and 6.

categories = ["billing", "account", "general"]

digit1 = 1
digit2 = 6

category1 = categories[digit1 % 3]   
category2 = categories[digit2 % 3]   


fixed_entries = [
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
    }
]


personalized_entries = [
    {
        "question": "how do i update my registered mobile number",
        "answer": "Go to Settings > Account Details and update your registered mobile number.",
        "keywords": "mobile number update",
        "category": category1
    },
    {
        "question": "how can i check my latest fee payment status",
        "answer": "You can check your latest fee payment status from the payments section of your account.",
        "keywords": "fee payment status",
        "category": category2
    }
]


faq_entries = fixed_entries + personalized_entries


df = pd.DataFrame(faq_entries)

print("Final 6-row FAQ DataFrame:")
print(df)
