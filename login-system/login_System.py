#This application serves as a login interface.
import getpass
from pathlib import Path
import csv
import pandas as pd

csvfile = Path("./users.csv")
csvfile1 = Path("./passwords.csv")
users = list(pd.read_csv("users.csv"))
passwords = list(pd.read_csv("passwords.csv"))

def writeUsersCSV():
     with open(csvfile, 'w', encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in users:
            writer.writerow(val) 

def writePasswordCSV():
    with open(csvfile1, 'w', encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in passwords:
            writer.writerow(val)
 
def get_User():
    uname = input("Input new Username: ")
    for x in users:
        if uname == x: 
            print("Username already in use!")
            exit    
        else:
            print("Username accepted!")
            users.append(uname)
            
def get_Pass():
    passw = getpass.getpass("Input new Password:")
    passwords.append(passw)

index = input("Sign up or sign in? ")

if index == "Sign up" or index == "sign up":
    get_User()
    get_Pass()
    writeUsersCSV()
    writePasswordCSV()
else:
    access = False 
    while access == False : 
        uname = input("Username: ")
        for x in users:
            if uname == x :
                print("Username accepted.")
            else:
                print("Username not on the list.")
                access = True

        if access == True :
            continue
        else:
            passw = getpass.getpass("Password: ")
            for x in passwords:
                if passw == x :
                    access = True
                    print("Access granted!")
                else:

                    access = False
                    print("Access denied. Try again...")

