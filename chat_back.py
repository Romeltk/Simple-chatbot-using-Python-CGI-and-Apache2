#!/usr/bin/env python3
print("Content-type:text/html\r\n\r\n")
import cgi, cgitb; cgitb.enable()

# Import modules for CGI handling 
import pandas

import random

# Dictionary of sample responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm good, how about you?", "Pretty good!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "name": ["My name is Chatbot.", "You can call me Chatbot.", "I'm Chatbot!"],
    "age": ["I'm just a computer program, so I don't have an age.", "Age is just a number for me!"],
    "location": ["I exist in the digital realm, so I'm everywhere and nowhere at the same time.", "I'm located wherever I'm needed, usually on servers."],
    "default": ["I'm not sure what you mean...", "Can you please rephrase that?", "I didn't understand that."]
}

# Function to generate bot response
def generate_bot_response(user_input):
    # Convert input to lowercase 
    user_input_lower = user_input.lower()

    # Check if input matches any predefined responses
    for key in responses:
        if key in user_input_lower:
            return random.choice(responses[key])

    # If no predefined response matches, return a default response
    return random.choice(responses["default"])


def parse_form_data():
    form = cgi.FieldStorage()
    user_input = form.getvalue('user_input')
    return user_input

# Function to generate HTML response
def generate_response(bot_response):
    print ("Content-type:text/html\r\n\r\n")
    print(f"""
    <html>
    <head>
        <title>Chatbot Response</title>
    </head>
    <body>
        <h1>Chatbot Response</h1>
        <p>{bot_response}</p>
    </body>
    </html>
    """)

# Main function
if __name__ == "__main__":
    user_input = parse_form_data()
    bot_response = generate_bot_response(user_input)
    generate_response(bot_response)
