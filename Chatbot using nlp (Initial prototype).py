
import random
import emojis
from datetime import datetime
import spacy

nlp = spacy.load("en_core_web_md")


# Define rules for responses based on keywords
Training_data = {
    "greeting": [
        "hi", "hello", "hey there", "hey",
        "hello there", "hi there", "good morning", "good evening"
    ],
    "farewell": [
        "bye", "see you", "goodbye", "talk to you later",
        "catch you later", "farewell"
    ],
    "help": [
        "can you help me", "i need assistance", "help me",
        "could you help", "i need some help", "help?"
    ],
    "thanks": [
        "thanks", "thank you", "appreciate it",
        "thank you so much", "thanks a lot"
    ],
    "time": [
        "what time is it", "tell me the time",
        "can you give me the current time", "current time please"
    ]
    # You can add more intents here (e.g. "about product", "hours", "contact", etc.)
}

intent_vectors={}
for intent, phrases in Training_data.items():
        intent_vectors[intent]= [nlp(phrase) for phrase in phrases]

intent_responses = {
    "greeting": [
        "Hi there! How can I help you today?",
        "Hello! What can I do for you?",
        "Hey! How's it going?"
    ],
    "farewell": [
        "Goodbye! Have a nice day.",
        "See you later! Take care.",
        "Bye! Come back if you need more help."
    ],
    "help": [
        "Sure, I'm here to help! What do you need?",
        "I'm at your service. Let me know how I can help.",
        "Of course. Tell me more about the issue."
    ],
    "thanks": [
        "You're welcome!",
        "No problem! Glad to help.",
        "Happy to help!"
    ],
    "time": [

        "Let me check the clock for you...",
        "It's time for some helpful info, but let me see..."
    ],
    "unknown": [
        "I'm not sure I understand. Could you rephrase?",
        "Sorry, I didn't get that. Can you try again?",
        "Hmm, I'm not certain I'm following you."
    ]
}

def classify_intent(user_input, threshold=0.65):
    """Return the best matching intent or 'unknown' if none match well."""
    doc = nlp(user_input.lower())
    best_intent = "unknown"
    best_score = 0.0

    for intent, vectors in intent_vectors.items():
        for vector_doc in vectors:
            similarity = doc.similarity(vector_doc)
            if similarity > best_score:
                best_score = similarity
                best_intent = intent

    # Only assign the best intent if the similarity is above a threshold
    if best_score < threshold:
        return "unknown"
    return best_intent

def get_current_time_response():
    """Return a user-friendly time-based message."""
    now = datetime.now()
    return f"The current time is {now.strftime('%H:%M:%S')}."

def get_response(user_input):
    """Based on user input, classify intent and return an appropriate response."""
    intent = classify_intent(user_input)

    # If user asked for time, handle that separately
    if intent == "time":
        # We can combine a standard response + specific time
        general_time_response = random.choice(intent_responses["time"])
        actual_time = get_current_time_response()
        return f"{general_time_response}\n{actual_time}"

    # Otherwise, give a random response from the matched intent
    return random.choice(intent_responses[intent])
def greet_user():
    """Return a greeting based on the time of day."""
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning! How can I help you today?"
    elif 12 <= current_hour < 18:
        return "Good afternoon! How can I help you today?"
    else:
        return "Good evening! How can I help you today?"

def chatbot():
    print("Chatbot:", greet_user())
    print("Type 'exit' or 'quit' to end the chat.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot:", random.choice(intent_responses["farewell"]))
            break

        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()



