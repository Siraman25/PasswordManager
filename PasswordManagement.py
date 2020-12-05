"""
Python Password Manager Framework - Password management system

(c) Aris Mandolini 2020 - Python Password Manager PPM
04.12.2020
"""

import os

"""
Lists all passwords and puts them in a dictionary with key: number, value: password txt file
Aris Mandolini
05.12.2020
"""


def pwListingDictionary():
    passwordList = os.listdir("UserData/Saves")
    i = 1
    passwordDictionary = {}
    for m in passwordList:
        passwordDictionary[i] = m
        i = i + 1
    return passwordDictionary


def pwListing():
    passwordList = os.listdir("UserData/Saves")
    i = 0
    for n in passwordList:
        passwordList[i] = n.rstrip(".txt")
        i = i + 1
    return passwordList


"""
Initiates the password management system, calls other functions
Aris Mandolini
04.12.2020
"""


def mainMangement():
    print("Welcome to your password manager.")
    print("Here you will be able to read, modify or delete your passwords.")
    print("Available commands:")
    print("  - Read or r + number from 1 - x: Password selector from list (read mode)")
    print("  - Delete or d + number from 1 - x: Password selector from list (delete mode)")
    print("  - Modify or m + number from 1 - x: Password selector from list (modify mode)")
    print("  - Back or b: Back to GUI selection screen")
    i = 1
    passwordList = pwListing()
    for n in passwordList:
        print(f"{i} - {n}")
        i = i + 1
    selector = input("What do you want to do? ")
    print(selector.replace(" ", "")[:-1])       # ONLY TEMPORARY
    if selector.replace(" ", "").lower()[:-1] == "read" or selector.replace(" ", "").lower()[:-1] == "r":
        print("read")       # TODO: Create read subsystems with relative functions
    elif selector.replace(" ", "").lower()[:-1] == "delete" or selector.replace(" ", "").lower()[:-1] == "d":
        print("delete")     # TODO: Create delete subsystems with relative functions
    elif selector.replace(" ", "").lower()[:-1] == "modify" or selector.replace(" ", "").lower()[:-1] == "m":
        print("modify")     # TODO: Create modify subsystems with relative functions
    elif selector.replace(" ", "").lower() == "back" or selector.replace(" ", "").lower() == "b":
        print("back")       # TODO: Create program exit control


# mainMangement()     # For debugging use
