def get_welcome_message(name):
    return f"Welcome, {name}! We're excited to have you here! 🎉"

def main():
    print("Hello! Let's get to know each other.")
    name = input("What's your name? ")
    welcome_message = get_welcome_message(name)
    print("\n" + welcome_message)

if __name__ == "__main__":
    main() 