# Accepting and Using Command Line Arguments

def greeting(name, language):
    greetings_language = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo"
    }
    message = f"{greetings_language[language]} {name}!"
    print(message)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personal greetings")

    parser.add_argument(
        "-n", "--name", 
        metavar="name", 
        required=True, 
        help="Name of the person to greet."
        )
    
    parser.add_argument(
        "-l", "--lang", 
        metavar="language", 
        required=True, 
        help="The language of greeting."
        )
    
    args = parser.parse_args()
    greeting(args.name, args.lang)
