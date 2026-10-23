# UCS420: Cognitive Computing - Assignment 7 (NLP-I)
# Q5. Corpus statistics
# Roll number: 1024170416

from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from nltk import bigrams
from nltk.stem import PorterStemmer
from starter import df, is_punct, process_ticket

results = [process_ticket(text) for text in df["Ticket_Text"]]
porter = PorterStemmer()

# Each set is kept per ticket, so bigrams never join the last word of one ticket to the first of the next.
sets = {
    "S1": [r["tokens"] for r in results],                                   # all tokens
    "S2": [[t for t in r["tokens"] if not is_punct(t)] for r in results],   # without punctuation
    "S3": [r["final"] for r in results],                                    # final tokens
}
sets["S4"] = [[porter.stem(t) for t in ticket] for ticket in sets["S3"]]   # S3 after Porter stemming
flat = {name: [t for ticket in tickets for t in ticket] for name, tickets in sets.items()}

# Total tokens, unique tokens and TTR (type-token ratio = unique / total)
stats = pd.DataFrame([
    {"Set": name, "Total_Tokens": len(tokens), "Unique_Tokens": len(set(tokens)),
     "TTR": round(len(set(tokens)) / len(tokens), 3)}
    for name, tokens in flat.items()
])
print(stats.to_string(index=False))

# 1. Top 10 words of S1 and S3
for name in ["S1", "S3"]:
    print(f"\nTop 10 words of {name}:", Counter(flat[name]).most_common(10))

# 2. log(rank) vs log(frequency) for S3 (Zipf plot)
freqs = sorted(Counter(flat["S3"]).values(), reverse=True)
ranks = np.arange(1, len(freqs) + 1)
plt.figure(figsize=(6, 4))
plt.plot(np.log(ranks), np.log(freqs), marker="o")
plt.xlabel("log(rank)")
plt.ylabel("log(frequency)")
plt.title("Zipf plot of S3 (final tokens) - roll no. 1024170416")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plot_path = Path(__file__).parent / "q5_zipf_S3.png"
plt.savefig(plot_path, dpi=150)
print(f"\nZipf plot saved to {plot_path.name}")

# 3. Top 5 bigrams of S1 and S3
for name in ["S1", "S3"]:
    pairs = Counter(pair for ticket in sets[name] for pair in bigrams(ticket))
    print(f"\nTop 5 bigrams of {name}:", pairs.most_common(5))

plt.show()

# Observe (starter notebook): Why does TTR change from S1 to S4 in your data?
# Answer: see q6_interpretation.md, part (a).
