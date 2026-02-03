# BASIC RULE-BASED CHATBOT WITH MORE RULES

def chatbot_reply(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "hi":
        return "Hello!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "My name is SimpleBot."
    elif user_input == "help":
        return "You can say hello, ask how I am, or type bye to exit."
    elif user_input == "thanks":
        return "You're welcome!"
    elif user_input == "bye":
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand."

print("🤖 SimpleBot is running (type 'bye' to exit)")

while True:
    user_message = input("You: ")
    response = chatbot_reply(user_message)
    print("Bot:", response)

    if user_message.lower() == "bye":
        break
