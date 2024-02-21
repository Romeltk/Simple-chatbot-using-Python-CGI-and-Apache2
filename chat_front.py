#!/usr/bin/python3
print ("Content-type:text/html\r\n\r\n")
import cgi, cgitb; cgitb.enable()

# HTML content for the chatbot interface
print("""
<html>
<head>
    <title>Simple Chatbot</title>
</head>
<body>
    <h1>Simple Chatbot</h1>
    <form method="post" action="chat_back.py">
        <label for="user_input">You:</label><br>
        <input type="text" id="user_input" name="user_input"><br><br>
        <input type="submit" value="Send">
    </form>
</body>
</html>
""")
