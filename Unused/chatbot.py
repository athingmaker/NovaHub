import nltk
import json
import random
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load the intents JSON file
with open('intents.json') as file:
    intents = json.load(file)

# Prepare the data for training
patterns = []
responses = []
tags = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize each word in the pattern
        words = nltk.word_tokenize(pattern)
        patterns.append(' '.join(words))
        responses.append(intent['responses'])
        tags.append(intent['tag'])

# Lemmatize and vectorize the text data
def clean_up_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    words = [lemmatizer.lemmatize(w.lower()) for w in words]
    return words

# Create feature vectors using TF-IDF
vectorizer = TfidfVectorizer(tokenizer=clean_up_sentence)

# Vectorize patterns
X = vectorizer.fit_transform(patterns)

# Encode tags
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(tags)

# Train the model using a Support Vector Classifier
model = SVC(kernel='linear')
model.fit(X, y)

# Define a function to get the bot's response
def respond_to_user(input_text):
    input_text = input_text.lower()
    input_vector = vectorizer.transform([input_text])
    prediction = model.predict(input_vector)
    tag = label_encoder.inverse_transform(prediction)[0]

    # Find the intent that matches the tag and return a random response
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

    return "Sorry, I didn't understand that."

# Chat loop
print("Chatbot: Hello! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = respond_to_user(user_input)
    print(f"Chatbot: {response}")