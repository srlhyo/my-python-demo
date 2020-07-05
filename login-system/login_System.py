#This application serves as a login interface.
import getpass
from pathlib import Path
import csv

csvfile = Path("./users.csv")
csvfile1 = Path("./passwords.csv")
users = []
passwords = []
with open(csvfile, newline = '') as f:
    reader = csv.reader(f)
    users = list(reader)
with open(csvfile1, newline = '') as f:
    reader = csv.reader(f)
    passwords = list(reader)

 
 
index = input("Sign up or sign in? ")

if index == "Sign up" or index == "sign up":
    uname = input("Input new Username: ")
    passw = getpass.getpass("Input new Password:")
    users.append(uname)
    passwords.append(passw)

    with open(csvfile, 'w') as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in users:
            writer.writerow([val]) 

    with open(csvfile1, 'w') as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in passwords:
            writer.writerow([val])
    
else:
    access = False 

    while access == False : 

        try:
            uname = input("Username: ")
            uindex = users.index(uname)
            matchPass = passwords.index(uindex)
            passw = getpass.getpass("Password: ")
        except ValueError as err:
            print(err)
            break


        if passw == matchPass :
            
            access = True
            print("Access granted!")

        else:

            access = False
            print("Access denied. Try again...")

