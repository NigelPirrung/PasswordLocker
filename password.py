import string
import random
import sys
import json


#Dictionary to hold accounts and passwords
accounts = {}

#Method to save the accounts into the file
def saveFile():
    with open('uploading.txt','w') as convert_file:
        convert_file.write(json.dumps(accounts))

#Method to load the accounts from the file
def loadAccounts():
    with open('uploading.txt') as f:
        
        tmp = json.loads(f.read())
        accounts.update(tmp)

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

            if change in accounts.keys():
                print("1. Change password \n2. New generated password")
                usrInput = int(input("Your Choice: "))
                
                if usrInput == 1:
                    newPass = input("New Password: ")
                    newPass = newPass.strip()
                    accounts[change] = newPass
                    saveFile()

                elif usrInput == 2:
                    newLength = int(input("Enter password length: "))
                    accounts[change] = generatePassword(newLength)
                    saveFile()

                else:
                    print("Invalid Option")
            else:
                print("\nAccount not found")

        elif choice == 3:
            if accounts:
                for key, value in accounts.items():
                    print("\n", key,"\n", value)
            else:
                print("\nNo saved accounts found\n")

        elif choice == 4:
            removeAccount = input("Account name: ")
            removeAccount = removeAccount.strip()

            if removeAccount in accounts.keys():
                accounts.pop(removeAccount)
                print(f"\tAccount {removeAccount} removed ")
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
loadAccounts()
choice = 0
while choice != 6:
    print("Password Manager: \n 1. Add a new account\n 2. Change existing account\n 3. View accounts \n 4. Delete account \n 5. Save \n 6. Exit")
    choice = input("Your Choice: ")

    if choice.isdigit() == False:
        choice = int(input("Incorrect Selection,Please enter another choice: "))
    else :
        choice = int(choice)
    
    
    userChoice(choice)


