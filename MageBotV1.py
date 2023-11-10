import subprocess
import os

def display_welcome_message():
    """Display the welcome message with ASCII art."""
    ascii_art = """
          ____
        ,'  , `.                                    ,---,.               ___
     ,-+-,.' _ |                                  ,'  .'  \            ,--.'|_
  ,-+-. ;   , ||                                ,---.' .' |   ,---.    |  | :,'
 ,--.'|'   |  ;|             ,----._,.          |   |  |: |  '   ,'\   :  : ' :
|   |  ,', |  ':  ,--.--.   /   /  ' /   ,---.  :   :  :  / /   /   |.;__,'  /
|   | /  | |  || /       \ |   :     |  /     \ :   |    ; .   ; ,. :|  |   |
'   | :  | :  |,.--.  .-. ||   | .\  . /    /  ||   :     \'   | |: ::__,'| :
;   . |  ; |--'  \__\/: . ..   ; ';  |.    ' / ||   |   . |'   | .; :  '  : |__
|   : |  | ,     ," .--.; |'   .   . |'   ;   /|'   :  '; ||   :    |  |  | '.'|
|   : '  |/     /  /  ,.  | `---`-'| |'   |  / ||   |  | ;  \   \  /   ;  :    ;
;   | |`-'     ;  :   .'   \.'__/\_: ||   :    ||   :   /    `----'    |  ,   /
|   ;/         |  ,     .-./|   :    : \   \  / |   | ,'                ---`-'
'---'           `--`---'     \   \  /   `----'  `----'
                              `--`-'
"""
    print(ascii_art)

def get_user_name():
    """Get the user's name."""
    return input("Enter your name: ")

def handle_master_options(name):
    """Handle options for the master user."""
    print(f"Greetings Master {name}, how can I assist you?")
    print("Options: ")
    print("1. Create ")
    print("2. Update ")

    option = input("Enter your choice (1 or 2): ")

    if option == "1":
        create_new_file()
    elif option == "2":
        update_existing_file()
    else:
        print("Invalid option. Please try again.")

def create_new_file():
    """Create and open a new Python file in nano."""
    subprocess.run(["nano", "new.py"])

def update_existing_file():
    """Update an existing file by opening it in nano."""
    files = os.listdir(os.getcwd())
    print("Existing files in the current directory:")
    for file in files:
        print(file)

    file_to_open = input("Enter the name of the file to open in nano: ")

    if file_to_open in files:
        subprocess.run(["nano", file_to_open])
    else:
        print("File not found. Please try again.")

def main():
    display_welcome_message()
    name = get_user_name()

    if name.lower() == "mage":
        handle_master_options(name)
    else:
        print(f"""                                                                                        

                ░░░░

                                            ██
                                          ██░░██
  ░░          ░░                        ██░░░░░░██                            ░░░░
                                      ██░░░░░░░░░░██
                                      ██░░░░░░░░░░██
                                    ██░░░░░░░░░░░░░░██
                                  ██░░░░░░██████░░░░░░██
                                  ██░░░░░░██████░░░░░░██
                                ██░░░░░░░░██████░░░░░░░░██
                                ██░░░░░░░░██████░░░░░░░░██
                              ██░░░░░░░░░░██████░░░░░░░░░░██
                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██
                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██
                          ██░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░██
                          ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██
                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██
                      ██░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░██
        ░░            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
                        ██████████████████████████████████████████




                  ░░
Greetings, {name}! Unfortunately, we are currently under construction. Please come back later.""")

if __name__ == "__main__":
    main()
