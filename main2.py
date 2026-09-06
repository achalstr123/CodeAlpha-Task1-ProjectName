# Basic Chatbot in Python
# CodeAlpha Internship Project

print("AI Chatbot: Hello! I am your basic chatbot.")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hello", "hi", "hey"]:
        print("AI Chatbot: Hello! How are you?")

    elif "how are you" in user_input:
        print("AI Chatbot: I am fine! Thank you for asking.")

    elif "your name" in user_input:
        print("AI Chatbot: My name is AI Chatbot.")

    elif "help" in user_input:
        print("AI Chatbot: I can answer basic questions. Try saying hello!")

    elif "python" in user_input:
        print("AI Chatbot: Python is a popular programming language.")

    elif "thank" in user_input:
        print("AI Chatbot: You're welcome! 😊")

    elif user_input in ["bye", "exit", "quit"]:
        print("AI Chatbot: Goodbye! Have a nice day. 👋")
        break

    else:
        print("AI Chatbot: Sorry, I don't understand that. Please try something else.")