# UCS420: Cognitive Computing - Assignment 7 (NLP-I)
# Q1. Preprocessing
# Roll number: 1024170416

import pandas as pd
from starter import df, FOCUS, FINGERPRINT, process_ticket

print(f"Fingerprint: {FINGERPRINT}   Tickets: {len(df)}\n")

# Run the official pipeline on every ticket
results = {tid: process_ticket(text) for tid, text in zip(df["Ticket_ID"], df["Ticket_Text"])}

table = pd.DataFrame([
    {
        "Ticket_ID": tid,
        "Sentences": len(r["sentences"]),
        "Tokens": len(r["tokens"]),
        "Punctuation": len(r["punct"]),
        "Stopwords": len(r["stops"]),
        "Unique_Tokens": len(set(r["tokens"])),
        "Final_Tokens": len(r["final"]),
    }
    for tid, r in results.items()
])

# TOTAL row: the counts are summed. Unique_Tokens is the number of distinct tokens across ALL tickets,
# because adding the per-ticket unique counts would count a shared word (e.g. "the") once per ticket.
total = table.drop(columns="Ticket_ID").sum().to_dict()
total["Unique_Tokens"] = len({t for r in results.values() for t in r["tokens"]})
table = pd.concat([table, pd.DataFrame([{"Ticket_ID": "TOTAL", **total}])], ignore_index=True)
print(table.to_string(index=False))

# Detailed view of one selected ticket (the first focus ticket the starter picked for this roll number)
tid = FOCUS[0]
r = results[tid]
print(f"\nSelected ticket {tid}: {df.loc[df['Ticket_ID'] == tid, 'Ticket_Text'].item()}")
print("  Tokens            :", r["tokens"])
print("  Punctuation tokens:", r["punct"])
print("  Stopwords         :", r["stops"])
print("  Final tokens      :", r["final"])

# Observe: final tokens that are not real words
all_final = sorted({t for r in results.values() for t in r["final"]})
not_words = [t for t in all_final if not t.replace("-", "").isalpha() or t == "ca"]  # wi-fi is a real word
print("\nFinal tokens that are not real words:", not_words)

# Observe (starter notebook): Which final tokens are not real words (e.g. n't, 's, ca)? Where do they come from?
# Answer: "ca" and "n't" come from word_tokenize splitting the contractions "can't" -> "ca" + "n't" and
# "didn't" -> "did" + "n't"; "did" is a stopword and gets removed, but "ca" and "n't" are not in the stopword
# list, so they survive into the final tokens. "+91", "98765", "43210", "0175-239-3201" and "3.12" are
# numbers (a phone number split into pieces and a version), not words; "wi-fi" is a real word kept whole.
