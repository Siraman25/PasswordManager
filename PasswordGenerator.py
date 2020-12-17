"""
Python Password Manager Framework - Password generation system

(c) Aris Mandolini 2020 - Python Password Manager PPM
02.12.2020
"""

import random
import os

"""
Generates actual Password with parameters queried before
Aris Mandolini
01.12.2020
"""


def PasswordGeneration(numsel, charsel, length):        # Functions that defines character ranges and generates the pw
    if numsel is False and charsel is False:        # NO numbers / NO spec characters
        minNumber1 = 65
        maxNumber1 = 91
        minNumber2 = 97
        maxNumber2 = 123
        numAmount = 2
    elif numsel is False and charsel is True:       # NO numbers / YES spec characters
        minNumber1 = 33
        maxNumber1 = 48
        minNumber2 = 58
        maxNumber2 = 127
        numAmount = 2
    elif numsel is True and charsel is False:       # YES numbers / NO spec characters
        minNumber1 = 48
        maxNumber1 = 58
        minNumber2 = 65
        maxNumber2 = 91
        minNumber3 = 97
        maxNumber3 = 123
        numAmount = 3
    elif numsel is True and charsel is True:        # YES numbers / YES spec characters
        minNumber1 = 33
        maxNumber1 = 127
        numAmount = 1

    if numAmount == 3:      # Creates a full list with the password range
        finallist = [*range(minNumber1, maxNumber1)] + [*range(minNumber2, maxNumber2)] + [*range(minNumber3, maxNumber3)]
    elif numAmount == 2:
        finallist = [*range(minNumber1, maxNumber1)] + [*range(minNumber2, maxNumber2)]
    else:
        finallist = [*range(minNumber1, maxNumber1)]

    ASCIIkey = []       # array initialization (storage of ASCII chars in DEC)
    for i in range(0, length, 1):       # loop to fill array from index 0 to charNumber-1
        ASCIIkey.append(random.choice(finallist))       # Selects a pseudo-random value from the given list and adds it

    generatedPassword = ""
    for val in ASCIIkey:
        generatedPassword = generatedPassword + chr(val)        # Converts ASCII DEC chars to a string variable

    return generatedPassword


"""
Adds data to file for storage and checks if the file doesn't already exist
Aris Mandolini
02.12.2020
"""


def addChecker(wsName, wsUrl, generatedPassword, nameloop):
    while nameloop:
        if wsName == "":
            wsName = input("The name cannot be void. Please change: ")
            nameloop = True
        elif os.path.isfile("UserData/Saves/" + wsName.lower() + ".txt"):
            nameloop = True
            wsName = input("Name already in use. Please change: ")
        else:
            fileOpen = open("UserData/Saves/" + wsName.lower() + ".txt", "a")
            fileOpen.write(wsName)
            fileOpen.write("\n" + wsUrl)
            fileOpen.write("\n" + generatedPassword)
            nameloop = False
            print("Password succesfully added!")


"""
Main program for password generation, declare and defines variables, calls other functions
Aris Mandolini
04.12.2020
"""


def mainPasswordGenerator():
    # Here starts the main subprogram
    webSiteName = input("Write a name for your website: ")
    webSiteUrl = input("Write the url of the website: ")
    numberSelector = input("Do you want to use numbers (default [RETURN]: yes)/no)? ")
    specCharSelector = input("Do you want to use special characters (default [RETURN]: yes)/no)? ")
    passwordLength = int(input("How long do you want your password to be? "))
    print()
    print("Thank you. We are generating your password.")
    # Checks number selection
    numberSelector = bool(numberSelector.lower() == "" or numberSelector.lower() == "yes" or numberSelector.lower() == "y")

    # Checks special characters selection
    specCharSelector = bool(specCharSelector.lower() == "" or specCharSelector.lower() == "yes" or specCharSelector.lower() == "y")

    nameloop = True
    # Calls addChecker function, which checks and saves the password, before being called it calls function
    # PasswordFunction, which generates the password based on the arguments given in mainPasswordGenerator
    addChecker(webSiteName, webSiteUrl, PasswordGeneration(numberSelector, specCharSelector, passwordLength), nameloop)


# mainPasswordGenerator()     # For debugging use
