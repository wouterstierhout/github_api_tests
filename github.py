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
        print
        print "[*] Github CLI Tool help page"
        print "help - show this"
        print "info - show url's"
        print "events - shows all events"
        print "gists - get list of gists"
        print
    elif (command == "get_info" or command == "info"):
        github_network.getInfo()
    elif (command == "get_events" or command == "events"):
        github_network.getEvents()
    elif (command == "gists"):
        github_network.getGists()
    elif (command == "exit" or command == "quit"):
        quit()
    else:
        print "github: "+command+" not found"
        
    askInput()    
    
# Login and Redirect to main function
if __name__ == "__main__":
    github_network.logIn()
    main()