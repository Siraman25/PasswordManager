"""
Python Password Manager Framework - Login system

(c) Aris Mandolini 2020 - Python Password Manager PPM
24.11.2020
"""

import os
from time import sleep

"""
Screen clearing function for Console-Execution (Bash/CMD)
Aris Mandolini
24.11.2020
"""
def clearScreenConsole():
    if os.name == 'nt':     # for windows
        _ = os.system('cls')
    else:
        _ = os.system('clear')  # for mac and linux     (posix)


"""
Screen clearing function for PyCharm-Execution (Print lines without Bash/CMD)
Aris Mandolini
24.11.2020
"""
def clearScreenNormal():
    print("\n"*100)     # Prints 100 clear lines


"""
User-creating function for username storage and password.
Aris Mandolini
24.11.2020
"""
def registeredUser(username, password):
    fileOpenNew = open("UserData/" + username.lower() + ".txt", "a")        # Opens (creates) new user file
    fileOpenNew.write("Account correct.")       # Adds correction statement to user account
    fileOpenNew.write("\nPassword:")
    fileOpenNew.write("\n" + password)      # Writes password in new line
    fileOpenNew.close()     # Closes file


"""
Main login function, which is being called by other Modules. It handles login and registration.
Aris Mandolini
24.11.2020
"""
def loginFunction():

    loginLoop = 1
    while loginLoop == 1:

        clearScreenNormal()     # Clears screen
        clearScreenConsole()
        print("Welcome to PPM v0.1")
        print("Please login. Write REGISTER in the Username field to create a new account.")
        print()
        username = input("Username: ")
        if username.lower() == "register":      # Checks if register option is selected
            registerLoop = 1
            while registerLoop == 1:
                setUsername = input("Please select a new Username: ")       # Allocates new username
                if os.path.isfile("UserData/" + setUsername.lower() + ".txt"):  # Checks if user (file) already exists
                    print("Username already in use.")
                    registerLoop = 1
                    sleep(5)
                else:
                    passwordLoop = 1
                    while passwordLoop == 1:
                        setPassword = input("Please select a new Password: ")       # Allocates new password
                        confirmPassword = input("Please confirm Password: ")
                        if setPassword == confirmPassword:      # Checks if password correct
                            passwordLoop = 0
                        else:
                            print("Wrong password. Please try again.")
                            passwordLoop = 1
                            sleep(5)
                    registeredUser(setUsername, setPassword)        # Calls registeredUser function
                    print("Username set up complete. You may now log in.")
                    registerLoop = 0
                    sleep(5)

            loginLoop = 1
        else:
            if os.path.isfile("UserData/" + username.lower() + ".txt"):     # Checks if the user exists
                fileOpenRead = open("UserData/" + username.lower() + ".txt", "r")       # Opens user file in read mode
                readFirstLine = fileOpenRead.readline()     # Reads first line
                readThirdLine = fileOpenRead.readlines()        # Reads third line
                if readFirstLine == "Account correct.\n":       # Checks validity of user file
                    password = input("Password: ")      # Allocates password
                    if password == readThirdLine[1]:        # Checks validity of password
                        print("Welcome. Access Granted.")
                        sleep(5)
                    else:
                        print("Wrong password.")
                        sleep(5)
                    loginLoop = 0
            else:
                print("Account Username wrong.")
                loginLoop = 1
                sleep(5)


loginFunction()     # Calls loginFunction for testing purposes
