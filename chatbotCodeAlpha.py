def chatbot():
    print("=" * 40)
    print("Welcome to CodeBot!")
    print("Type 'help' to see commands.")
    print("Type 'bye' to exit.")
    print("=" * 40)

    while True:
        user = input("\nYou: ").lower().strip()

        if user == "hello" or user == "hi":
            print("CodeBot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("CodeBot: I'm fine, thanks for asking!")

        elif user == "what is your name":
            print("CodeBot: My name is CodeBot.")

        elif user == "who made you":
            print("CodeBot: I was created as a Python internship project by Shivansh Bajaj.")

        elif user == "help":
            print("\nAvailable Commands:")
            print("- hello / hi")
            print("- how are you")
            print("- what is your name")
            print("- who made you")
            print("- python")
            print("- date")
            print("- help")
            print("- bye")

        elif user == "python":
            print("CodeBot: Python is a popular programming language used for web development, AI, and automation.")

        elif user == "date":
            from datetime import datetime
            print("CodeBot:", datetime.now().strftime("%d-%m-%Y"))

        elif user == "bye":
            print("CodeBot: Goodbye! Have a great day.")
            break

        else:
            print("CodeBot: Sorry, I don't understand that command.")
            print("CodeBot: Type 'help' to see available commands.")

chatbot()