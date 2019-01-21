# @nameri

import time
import random

bot_template = "BOT: {0}"
user_template = "USER: {0}"

responses = {
    "What's your name?": [
        "My name is AlizIA. Nice to meet you.",
        "hAI! I'm AlizIA",
        "It's AlizIA here! How are you?"
    ],
    "How are you?": "I'm fine! Thank you!",
    "question":  "Don't know but I will be thinking about it the rest of the day",
    "statement": "I could agree... or not"
}

error = [
    "I can't understand you, can you explain it please?",
    "What do you mean?",
    "I need more information"
]

# Define a function that responds to a user's message: respond
def  respond(message):
    time.sleep(0.5)
    # Concatenate the user's message to the end of a standard bot response
    # bot_message = "I can hear you! You said: " + message

    if message.endswith("?") and message not in responses:
        # Return a random question
        return responses["question"]
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(error)

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
send_message("Find me?")
send_message("What's your name?")

