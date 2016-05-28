#!/usr/bin/python
import os
import github_network

# Simple Github CLI Tool
# Username: wouterstierhout
# Password: PythonTestingPassword

# Clear the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Starting function
def main():
    cls()
    print "Starting the Github CLI Tool"
    print
    askInput()
    
# Ask for Input in console    
def askInput():
    command = raw_input("Github:~$ ")
    executeCommand(command)   

# Execute the command from input and parse to output
def executeCommand(string):
    command = string.lower()
    if command == "help":
        print "hellpppppppp"
    elif (command == "get_info" or command == "info"):
        github_network.getInfo()
    elif (command == "exit" or command == "quit"):
        quit()
    else:
        print ""+command+" not found"
        
    askInput()    
    
# Login and Redirect to main function
if __name__ == "__main__":
    github_network.logIn()
    main()