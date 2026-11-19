import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Input

# 1. Training data: paragraph about cricket (approximately 100 words)
training_text = """
Cricket is a team sport played with a bat and ball.
Two teams compete to score runs and take wickets.
The batter watches the bowler carefully and chooses the right shot.
A fast bowler uses pace and swing, while a spin bowler changes
the flight and turn of the ball.
Fielders work together to stop runs and catch the ball.
The captain makes plans based on the pitch, weather, and match situation.
Good players practise regularly, stay patient, and support their teammates.
In a close match, every run matters.
Cricket teaches teamwork, discipline, confidence, and respect.
Fans enjoy the excitement of a boundary, a wicket, and a final-over victory.
"""

# 2. Tokenize the text using Keras Tokenizer
tokenizer = Tokenizer(oov_token="<OOV>")
sentences = [
    sentence.strip()
    for sentence in training_text.lower().split(".")
    if sentence.strip()
]

tokenizer.fit_on_texts(sentences)

total_words = len(tokenizer.word_index) + 1

print("Total unique tokens:", len(tokenizer.word_index))
print("\nWord Index:")
print(tokenizer.word_index)

# 3. Create input sequences
input_sequences = []

for sentence in sentences:
    token_list = tokenizer.texts_to_sequences([sentence])[0]

    # Create progressively longer sequences
    for i in range(2, len(token_list) + 1):
        input_sequences.append(token_list[:i])

# Pad sequences to equal length
max_sequence_len = max(len(seq) for seq in input_sequences)

input_sequences = pad_sequences(
    input_sequences,
    maxlen=max_sequence_len,
    padding='pre'
)

# Separate predictors and target words
X = input_sequences[:, :-1]
y = input_sequences[:, -1]

print("\nInput Sequence Shape:", X.shape)
print("Target Shape:", y.shape)

# 4. Build an LSTM model
model = Sequential([
    Input(shape=(max_sequence_len - 1,)),
    Embedding(
        input_dim=total_words,
        output_dim=32
    ),
    LSTM(64),
    Dense(total_words, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# 5. Train the model
model.fit(
    X,
    y,
    epochs=150,
    batch_size=16,
    verbose=1
)

# 6. Generate text from a seed word
def generate_text(seed_word, next_words=10):
    current_text = seed_word.lower()

    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([current_text])[0]

        padded_sequence = pad_sequences(
            [token_list],
            maxlen=max_sequence_len - 1,
            padding='pre'
        )

        predictions = model.predict(
            padded_sequence,
            verbose=0
        )[0]

        predicted_id = int(np.argmax(predictions))
        predicted_word = tokenizer.index_word.get(
            predicted_id, ""
        )

        if not predicted_word or predicted_word == "<OOV>":
            break

        current_text += " " + predicted_word

    return current_text.capitalize()

# 7. Generate three lines from three seed words
seed_words = ["cricket", "captain", "bowler"]

print("\nGenerated Text:")
for seed in seed_words:
    print(generate_text(seed, next_words=10))
