# UCS420: Cognitive Computing - Assignment 7 (NLP-I)
# Q2. Regex extraction and replacement
# Roll number: 1024170416

import re
from nltk.tokenize import sent_tokenize
from starter import df, TEST_LINES

# A word must not touch @ . / : - on its left, or @ / : - (or a dot followed by more text) on its right,
# so pieces of emails, URLs and hyphenated words ("thapar", "edu", "https", the "in" of "log-in")
# are not counted as separate words. (?<!\w') stops the "t" of "isn't" from starting a new word.
L = r"(?<![\w@./:-])(?<!\w')"
R = r"(?![\w@/:-]|\.\w)"

LONG_WORDS = L + r"[A-Za-z]{6,}" + R                                   # more than 5 letters
NUMBERS = r"\d+(?:,\d{3})*(?:\.\d+)*"                                  # 3.12, 95.5, 2.0.1, 1,250 stay whole
# (phone numbers come out as their digit groups here, e.g. 98765 and 43210; PHONE below handles them whole)
CAPITALIZED = L + r"[A-Z][A-Za-z]*(?:['-][A-Za-z]+)*" + R              # Call, MATLAB, Wi-Fi, Rao's
VOWEL_WORDS = L + r"[AEIOUaeiou][A-Za-z]*(?:['-][A-Za-z]+)*" + R       # isn't, e-mail, another

EMAIL = r"[\w.+-]+@[\w-]+(?:\.[\w-]+)*\.[A-Za-z]{2,}"
URL = r"(?:https?://|www\.)\S+?(?=[.,;:!?)]*(?:\s|$))"                # trailing punctuation is not part of the URL
PHONE = r"(?:\+\d{1,3}[\s-]?)?\b\d{5}[\s-]?\d{5}\b|\b\d{3,5}-\d{3,4}-\d{4}\b"   # +91 98765 43210, 0175-239-3201


def extract(text):
    return {
        "Words > 5 letters": re.findall(LONG_WORDS, text),
        "Numbers": re.findall(NUMBERS, text),
        "Capitalized words": re.findall(CAPITALIZED, text),
        "Vowel-initial words": re.findall(VOWEL_WORDS, text),
    }


def replace(text):
    text = re.sub(EMAIL, "<EMAIL>", text)  # emails first, so their domain is not mistaken for a URL
    text = re.sub(URL, "<URL>", text)
    return re.sub(PHONE, "<PHONE>", text)


for title, lines in [("TEST_LINES", TEST_LINES), ("My tickets", df["Ticket_Text"].tolist())]:
    print(f"========== {title} ==========")
    for line in lines:
        print("\n" + line)
        for name, found in extract(line).items():
            print(f"  {name:<20}: {found}")
        print(f"  {'After re.sub()':<20}: {replace(line)}")
    print()

# Observe: capitalized words that are capitalized only because they start a sentence.
# A sentence-initial word counts if it is not "I", not an acronym, and never appears capitalized mid-sentence.
starts, mid_sentence = [], set()
for text in df["Ticket_Text"]:
    for sentence in sent_tokenize(text):
        for m in re.finditer(CAPITALIZED, sentence):
            if m.start() == 0:
                starts.append(m.group())
            else:
                mid_sentence.add(m.group().lower())
start_only = [w for w in starts if w != "I" and not w.isupper() and w.lower() not in mid_sentence]
print(f"Capitalized only because they start a sentence ({len(start_only)} of {len(starts)} sentence-initial words):")
print(" ", start_only)

# Observe (starter notebook): How many of your capitalized words are capitalized only because they start a sentence?
# Answer: 14 of the 22 sentence-initial capitalized words - Please (4), Is (3), The (3), Student, Laptop,
# Can and Call. The other 8 are capitalized anyway: "I" (6 times) is always capital, and Python / Matlab
# are names that also appear capitalized in the middle of other sentences ("The Python", "the MATLAB").
# "Laptop" (T03) shows the effect clearly: the same ticket later writes it in lowercase, "my laptop".
