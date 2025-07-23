
import random
import emojis
from datetime import datetime

# Define rules for responses based on keywords
rules = {
    "hi": ["Hey there! ", "Hi, nice to see you!", "Hello!"],
    "hello": ["Hey there!", "Hi, nice to see you!", "Hello!"],
    "help": ["How can I assist you?", "I'm here to help! What's up?"],
    "bye": ["See you later!", "Goodbye!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "how are you": ["I'm good, thanks for asking!", "Doing well! How about you?"]
}
# Default responses for unmatched input
default_responses = ["Sorry, I didn't understand that.",
                     "Can you rephrase that?",
                     "I'm not sure what you mean. Try again!",
                     "Oops, I don't understand that. Please try again!"]

def get_time_response():

    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning! how can i help you?"
    elif 12 < current_hour < 17:
        return "Good afternoon! how can i help you?"
    else:
        return "Good evening! how can i help you?"

def get_response(user_input):

    user_input = user_input.lower()
    for keyword, response in rules.items():
        if keyword in user_input:
            return random.choice(response)

    return random.choice(default_responses)

def chatbot():
    print("Chatbot:", get_time_response())

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot:", random.choice(rules["bye"]))
            break
        response = get_response(user_input)
        print("Chatbot: ", response)

if __name__ == "__main__":
    chatbot()



