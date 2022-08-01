import string
import random
import sys
import json


#Dictionary to hold accounts and passwords
accounts = {}

def saveFile():
    with open('uploading.txt','w') as convert_file:
                    convert_file.write(json.dumps(accounts))

def loadAccounts():
    f = open("uploading.txt", "a")

    with open('uploading.txt') as f:
        read = f.read()
    accounts = json.loads()

#Function to generate password
def generatePassword(length): 
    
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    password = []

    while len(password)!= length:
        
        random.shuffle(characters)

        for i in range(length):
            password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)

#Function to perform operations based on user choice
def userChoice(choice):
    
        if choice == 1:
            account = input("Enter account:")
            account = account.strip()
            length = int(input("Enter password Length: "))
            accounts[account] = generatePassword(length)
            saveFile()
        elif choice == 2:
            
            change = input("Enter account name: ")

            
            print(accounts)

            if change in accounts:
                print("1. Change password \n2. New generated password")
                usrInput = int(input("Your Choice: "))
                
                if usrInput == 1:
                    newPass = input("New Password: ")
                    newPass = newPass.strip()
                    accounts[change] = newPass

                elif usrInput == 2:
                    newLength = int(input("Enter password length: "))
                    accounts[change] = generatePassword(newLength)

                else:
                    print("Invalid Option")
            else:
                print("\nAccount not found")

            saveFile()

        elif choice == 3:
            f = open("uploading.txt","r")
            print(f.read())
        
            
        elif choice == 4:
            removeAccount = input("Account name: ")
            removeAccount = removeAccount.strip()

            print(accounts.keys())

            if removeAccount in accounts.keys():
                accounts.pop(removeAccount)
                print(f"Account {removeAccount} removed ")
                saveFile()
            else :
                print("account not found")
            
        elif choice == 5:
                with open('uploading.txt','w') as convert_file:
                    convert_file.write(json.dumps(accounts))
                print("File Saved")
        elif choice == 6:
            sys.exit("Goodbye")
        else:
            print("Please enter a valid choice")


#Start of Program
#loadAccounts()
choice = 0
while choice != 6:
    print("Password Manager: \n 1. Add a new account\n 2. Change existing account\n 3. View accounts \n 4. Delete account \n 5. Save \n 6. Exit")
    choice = input("Your Choice: ")

    if choice.isdigit() == False:
        choice = int(input("Incorrect Selection,Please enter another choice: "))
    else :
        choice = int(choice)
    
    
    userChoice(choice)


