import subprocess
import os

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

# Taking user input for their name
name = input("Enter your name: ")

# Checking if the name is "Mage" or "mage"
if name.lower() == "mage":
    print(f"Greetings Master {name}, how can I assist you?")
    print("Options: ")
    print("1. Create ")
    print("2. Update ")
    
    # Taking user input for options
    option = input("Enter your choice (1 or 2): ")
    
    if option == "1":
        # Execute command to create and open a new Python file in nano
        subprocess.run(["nano", "new.py"])
    elif option == "2":
        # List files in the current directory
        files = os.listdir(os.getcwd())
        print("Existing files in the current directory:")
        for file in files:
            print(file)
        
        # Taking user input for the file to open
        file_to_open = input("Enter the name of the file to open in nano: ")
        
        # Check if the entered file exists in the directory
        if file_to_open in files:
            # Execute command to open the selected file in nano
            subprocess.run(["nano", file_to_open])
        else:
            print("File not found. Please try again.")
    else:
        print("Invalid option. Please try again.")
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
Greetings, {name}! Unfortunately we are currently under construction. Please come back later.""")
