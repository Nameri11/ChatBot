# @nameri

import time
import random

bot_template = "BOT: {0}"
user_template = "USER: {0}"

#Variables
name = "AlizIA"

responses = {
    "What's your name?": [
        "My name is {0}. Nice to meet you.".format(name),
        "hAI! I'm {0}".format(name),
        "It's {0} here! How are you?".format(name)
    ],
    "How are you?": "I'm fine! Thank you!",
    "question":  "Don't know but I will be thinking about it the rest of the day",
    "error": [
        "I could agree... or not",
        "I can't understand you, can you explain it please?",
        "What do you mean?",
        "I need more information"
    ]
}

# Define a function that responds to a user's message: respond
def  respond(message):
    time.sleep(0.5)
    # Concatenate the user's message to the end of a standard bot response
    # bot_message = "I can hear you! You said: " + message

    if message.endswith("?") and message not in responses:
        # Return a random question
        return responses["question"]
    if not message.endswith("?") and message not in responses:
        return random.choice(responses["error"])
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["error"])

    # Return the result
    return bot_message

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send a message to the bot
send_message("Find me")
send_message("What's your name?")
send_message("hello")

