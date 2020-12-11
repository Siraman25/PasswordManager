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
    passwordList = os.listdir("UserData/Saves")     # Gets list of passwords
    i = 1
    passwordDictionary = {}
    for m in passwordList:
        passwordDictionary[i] = m       # Fills dictionary with values from passwordList
        i = i + 1
    return passwordDictionary       # Returns the dictionary


"""
Lists all passwords and puts them in a list
Aris Mandolini
05.12.2020
"""


def pwListing():
    passwordList = os.listdir("UserData/Saves")     # Gets list of password
    i = 0
    for n in passwordList:
        passwordList[i] = n[:-4]        # Removes ".txt" extension from passwordList values
        i = i + 1
    return passwordList     # Returns the list


"""
Read subsystem, allows to read selected login information
Aris Mandolini
07.12.2020
"""


def readSubSys(selector, passDict):
    newselector = selector.lower().replace("read", "").replace("r", "").replace(" ", "")        # Formats the selector
    if int(newselector) in passDict:        # Checks if the selector value exists in passDict (password dictionary)
        fileTxt = (passDict[int(newselector)])      # Defines file name
        fileOpen = open("UserData/Saves/" + fileTxt, "r")       # Opens defined file
        readName = fileOpen.readline().replace('\n', '')        # Reads name
        readLines = fileOpen.readlines()        # Reads all lines from line 2+
        readUrl = readLines[0].replace('\n', '')        # Reads url
        readPass = readLines[1].replace('\n', '')       # Reads password
        print(f"Name: {readName}, URL: {readUrl}, Password: {readPass}")
    else:
        print("Please select a valid number")       # Prints error if exception


"""
Initiates the password management system, calls other functions
Aris Mandolini
04.12.2020
"""


def mainMangement():
    ManagementLoop = 1
    while ManagementLoop == 1:      # Repeats program until user stops it
        print("""
Welcome to your password manager.
Here you will be able to read, modify or delete your passwords.
Available commands:
    - Read or r + number from 1 - x: Password selector from list (read mode)
    - Delete or d + number from 1 - x: Password selector from list (delete mode)
    - Modify or m + number from 1 - x: Password selector from list (modify mode)
    - Back or b: Back to GUI selection screen""")
        i = 1
        passwordDictionary = pwListingDictionary()      # Calls pwListingDictionary() function, returns pw dict
        passwordList = pwListing()      # Calls pwListing() function, returns pw list
        for n in passwordList:      # Prints possible login selections
            print(f"{i} - {n}")
            i = i + 1
        selector = input("What do you want to do? ")
        # print(selector.replace(" ", "")[:-1])       # ONLY TEMPORARY

        # Checks selector command, calls other functions for each respective subsystem
        if selector.replace(" ", "").lower()[:-1] == "read" or selector.replace(" ", "").lower()[:-1] == "r":
            readSubSys(selector, passwordDictionary)        # Calls readSubSys function, read mode
        elif selector.replace(" ", "").lower()[:-1] == "delete" or selector.replace(" ", "").lower()[:-1] == "d":
            print("delete")     # TODO: Create delete subsystems with relative functions
        elif selector.replace(" ", "").lower()[:-1] == "modify" or selector.replace(" ", "").lower()[:-1] == "m":
            print("modify")     # TODO: Create modify subsystems with relative functions
        elif selector.replace(" ", "").lower() == "back" or selector.replace(" ", "").lower() == "b":
            print("back")       # TODONE: Create program exit control
            return "back"       # Returns "back" to mainManagement() function, brings user back to GUI.py


# mainMangement()     # For debugging use
