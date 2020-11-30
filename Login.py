"""
Python Password Manager Framework - Login system

(c) Aris Mandolini 2020 - Python Password Manager PPM
24.11.2020
"""

import os
from time import sleep


def clearScreenConsole():
    os.system("cls")
    if os.name == 'nt':     # for windows
        _ = os.system('cls')
    else:
        _ = os.system('clear')  # for mac and linux     (posix)


def clearScreenNormal():
    print("\n"*100)


def registeredUser(username, password):
    fileOpenNew = open("UserData/" + username.lower() + ".txt", "a")
    fileOpenNew.write("Account correct.")
    fileOpenNew.write("\nPassword:")
    fileOpenNew.write("\n" + password)
    fileOpenNew.close()


def loginFunction():

    loginLoop = 1
    while loginLoop == 1:

        clearScreenNormal()
        clearScreenConsole()
        print("Welcome to PPM v0.1")
        print("Please login. Write REGISTER in the Username field to create a new account.")
        print()
        username = input("Username: ")
        if username.lower() == "register":
            registerLoop = 1
            while registerLoop == 1:
                setUsername = input("Please select a new Username: ")
                if os.path.isfile("UserData/" + setUsername.lower() + ".txt"):  # DO JURI
                    print("Username already in use.")
                    registerLoop = 1
                    sleep(5)
                else:
                    passwordLoop = 1
                    while passwordLoop == 1:
                        setPassword = input("Please select a new Password: ")
                        confirmPassword = input("Please confirm Password: ")
                        if setPassword == confirmPassword:
                            passwordLoop = 0
                        else:
                            print("Wrong password. Please try again.")
                            passwordLoop = 1
                            sleep(5)
                    registeredUser(setUsername, setPassword)
                    print("Username set up complete. You may now log in.")
                    registerLoop = 0
                    sleep(5)

            loginLoop = 1
        else:
            if os.path.isfile("UserData/" + username.lower() + ".txt"):
                fileOpenRead = open("UserData/" + username.lower() + ".txt", "r")
                readFirstLine = fileOpenRead.readline()
                readThirdLine = fileOpenRead.readlines()
                if readFirstLine == "Account correct.\n":
                    password = input("Password: ")
                    if password == readThirdLine[1]:
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


loginFunction()

"""
Hoila des isch a kommentar.
"""