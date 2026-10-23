# UCS420: Cognitive Computing - Assignment 7 (NLP-I)
# Q3. Custom tokenization
# Roll number: 1024170416

from nltk.tokenize import RegexpTokenizer, word_tokenize
from starter import df, TEST_LINES

# One pattern; alternatives are tried in order, so the most specific token types come first.
PATTERN = r"""(?x)
    (?:https?://|www\.)\S+?(?=[.,;:!?)]*(?:\s|$))       # URLs (trailing punctuation left out)
  | [\w.+-]+@[\w-]+(?:\.[\w-]+)*\.[A-Za-z]{2,}          # email addresses
  | (?:\+\d{1,3}[\s-]?)?\d{5}[\s-]?\d{5}                # mobile numbers, optional +91 prefix
  | \d{3,5}-\d{3,4}-\d{4}                               # landline numbers like 0175-239-3201
  | \d+(?:,\d{3})*(?:\.\d+)*(?!\w)                      # numbers, decimals (95.5) and versions (2.0.1)
  | (?:[A-Za-z]\.){2,}                                  # abbreviations like p.m.
  | \w+(?:['-]\w+)*                                     # words, contractions (isn't), hyphenated (Wi-Fi)
  | \.\.\.                                              # ellipsis
  | [^\w\s]                                             # any other single punctuation mark
"""
tokenizer = RegexpTokenizer(PATTERN)


def my_tokenize(text):
    return tokenizer.tokenize(text)


# quick self-checks of the required token types
assert my_tokenize("The state-of-the-art Wi-Fi isn't 95.5% done.") == \
    ["The", "state-of-the-art", "Wi-Fi", "isn't", "95.5", "%", "done", "."]
assert my_tokenize("Version 2.0.1 at 5.30 p.m.") == ["Version", "2.0.1", "at", "5.30", "p.m."]
assert my_tokenize("Call +91 98765 43210 or 0175-239-3201.") == ["Call", "+91 98765 43210", "or", "0175-239-3201", "."]


def compare(text):
    mine, nltk_tokens = my_tokenize(text), word_tokenize(text)
    print("\n" + text)
    print("  my_tokenize  :", mine)
    print("  word_tokenize:", nltk_tokens)
    if mine != nltk_tokens:
        print("  only in my_tokenize  :", [t for t in mine if t not in nltk_tokens])
        print("  only in word_tokenize:", [t for t in nltk_tokens if t not in mine])
    return mine != nltk_tokens


print("========== TEST_LINES ==========")
for line in TEST_LINES:
    compare(line)

print("\n========== My tickets ==========")
different = [tid for tid, text in zip(df["Ticket_ID"], df["Ticket_Text"]) if compare(text)]
print(f"\nTickets tokenized differently: {len(different)} of {len(df)} -> {different}")

# Differences between my_tokenize and word_tokenize (seen in the output above):
# 1. Contractions: word_tokenize splits "can't" into "ca" + "n't" and "isn't" into "is" + "n't" (Penn Treebank
#    style, so the negation becomes its own token); my_tokenize keeps "can't" / "isn't" as one token.
# 2. Phone numbers: word_tokenize breaks "+91 98765 43210" into "+91", "98765", "43210" because it splits on
#    spaces; my_tokenize has a phone rule that matches the whole number, spaces included, as one token.
# 3. Emails: word_tokenize splits "it.helpdesk@thapar.edu" at the "@" into "it.helpdesk", "@", "thapar.edu";
#    my_tokenize matches the full email address first, so it stays one token.
# 4. URLs: word_tokenize splits "https://lms.thapar.edu/help" at the colon into "https", ":", "//lms.thapar.edu/help";
#    my_tokenize's URL rule keeps it whole and leaves out the sentence-ending full stop.
# Both tokenizers agree on hyphenated words (Wi-Fi, state-of-the-art), decimals (95.5) and versions (2.0.1).

# Observe (starter notebook): How many of your tickets are tokenized differently by my_tokenize and word_tokenize?
# Answer: 3 of 13 - T01 and T06 (the contractions "can't" / "didn't") and T07 (the phone number
# "+91 98765 43210"). The other 10 tickets contain only plain words, Wi-Fi, 3.12 and ordinary punctuation,
# which both tokenizers handle the same way.
