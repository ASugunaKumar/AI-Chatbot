import nltk
nltk.download('punkt')
import random
from datetime import datetime

# Define rules for responses based on keywords
rules = {
    "hi": ["Hey there!", "Hi, nice to see you!", "Hello!"],
    "hello": ["Hey there!", "Hi, nice to see you!", "Hello!"],
    "help": ["How can I assist you?", "I'm here to help! What's up?"],
    "bye": ["See you later!", "Goodbye!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "how are you": ["I'm good, thanks for asking!", "Doing well! How about you?"]
}
# Default responses for unmatched input
default_responses = ["Sorry, I didn't understand that.",
                     "Can you rephrase that?",
                     "I'm not sure what you mean. Try again!"]

def get_time_response():

    current_hour = datetime.now().hour
    if current_hour < 12:
        print("Good morning! how can i help you?")
    elif 12 < current_hour < 18:
        print("Good afternoon! how can i help you?")
    else:
        print("Good evening! how can i help you?")




