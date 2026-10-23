# UCS420: Cognitive Computing — Assignment 7 (NLP-I)
## Q6. Interpretation

Roll number: 1024170416 · Fingerprint: 714385E9 · 13 tickets

All numbers below come from running `q1`–`q5` on my generated dataset.

### (a) Why does TTR change from S1 to S4 in your dataset?

| Set | Total tokens | Unique tokens | TTR |
|-----|-------------:|--------------:|----:|
| S1 – all tokens | 152 | 77 | 0.507 |
| S2 – no punctuation | 127 | 73 | 0.575 |
| S3 – final tokens | 76 | 49 | 0.645 |
| S4 – S3 after Porter | 76 | 49 | 0.645 |

TTR goes up from S1 to S3 because each step removes the tokens that repeat the most.
In S1 the top tokens are `.` (16 times), `i` and `the` (8 each), `?` and `!`. Dropping punctuation
(S2) and then stopwords (S3) removes many tokens but very few *types*, so the tokens that remain are more
varied (unique ÷ total rises).

From S3 to S4 the TTR stays at 0.645. Stemming only lowers TTR when two different words share a stem
(e.g. "stop" and "stopped"). My tickets are short and each word appears in only one form: "stopped" but
never "stop", "installed" and "reinstalled" (which Porter keeps apart as `instal` / `reinstal`). So Porter
renames all 49 types without merging any of them.

### (b) One example where word_tokenize() and my tokenizer differ

Ticket T01, *"I can't login and I didn't change anything."*

- `word_tokenize`: `['I', 'ca', "n't", 'login', ...]`
- `my_tokenize`: `['I', "can't", 'login', ...]`

word_tokenize follows the Penn Treebank convention. It splits a contraction into the verb and a separate
`n't`, so negation becomes its own token. That leaves the fragment `ca`, which is not a word. My pattern
`\w+(?:['-]\w+)*` lets an apostrophe join two word parts, so `can't` stays one token. The same happens with
the phone number in T07: word_tokenize gives `+91`, `98765`, `43210`, and my phone rule keeps
`+91 98765 43210` whole.

### (c) One example where stemming produces an undesirable result

Lancaster turns **"portal"** into **`port`**. In IT-support tickets that is a real problem: a "student
portal" complaint and a "USB/network port" complaint would now look like the same word. Porter also turns
"anything" into `anyth` and "slowly" into `slowli`, which are not words at all.

### (d) One example where POS-aware lemmatization preserves meaning better than stemming

**"tried"** (tagged `VBD`, past-tense verb). Porter and Lancaster both give `tri`, which is not a word.
WordNet with the verb POS gives **`try`**: the real dictionary form, with the meaning intact. The POS
matters: without it the lemmatizer treats every word as a noun and would return "tried" unchanged.
