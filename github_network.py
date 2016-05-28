import requests
import time

username = ""
password = ""

def logIn():
    print "[*] Please login to Github"
    username = raw_input("username: ")
    password = raw_input("password: ")
    
    r = requests.get("https://api.github.com", auth=(username, password))
    
    if r.status_code == 200:
        print "[*] Succes"
        time.sleep(2)
    else:
        print "[*] Failed, try again"
        time.sleep(1)
        logIn()
        
def getInfo():
    r = requests.get("https://api.github.com", auth=(username, password))
    print r.text