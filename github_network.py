import requests
import time

username = None
password = None

def logIn():
    print "[*] Please login to Github"
    global username
    global password
    
    username = raw_input("username: ")
    password = raw_input("password: ")
    
    r = requests.get("https://api.github.com", auth=(username, password))
    
    if r.status_code == 200:
        print "[*] Success"
        print r.text
        time.sleep(2)
    else:
        print "[*] Failed, try again"
        time.sleep(1)
        logIn()
        
def getInfo():
    r = requests.get("https://api.github.com", auth=(username, password))
    print r.text
    
def getEvents():
    r = requests.get("https://api.github.com/events", auth=(username, password))
    print r.text
    
def getGists():
    r = requests.get("https://api.github.com/gists", auth=(username, password))
    print r.text