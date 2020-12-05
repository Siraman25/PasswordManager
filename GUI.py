"""
Python Password Manager Framework - GUI selection system

(c) Juri Ladurner, Aris Mandolini 2020 - Python Password Manager PPM
04.12.2020
"""

import sys
import PasswordGenerator
import PasswordManagement

"""
Program switcher for selection in function Menue // Updated switch_Menue function
Aris Mandolini, Juri Ladurner
05.11.2020
"""


def switch_Menue(inputchar):
    if inputchar == 1:
        PasswordGenerator.mainPasswordGenerator()       # Opens mainPasswordGenerator() funct. in PasswordGenerator mod.
    elif inputchar == 2:
        PasswordManagement.mainMangement()      # Opens mainManagement() function in PasswordManagement module
    else:
        sys.exit(0)     # Program exits with code 0


"""
Switch Case to open the subprograms // DEPRECATED
Juri Ladurner
30.11.2020
"""


def switch_Meenue(i):
    switcher = {        # Switch-case function for python
        1: print("a"),       # Starts the password generation
        2: print("1"),      # Starts the password management
        3: sys.exit(0)      # Program exits with code 0
    }
    return switcher.get(i, "Invalid day of week")


"""
The Menue where the user can decide with Subprograms he want to use
Juri Ladurner
30.11.2020
"""


def Menue():
    possibility = 7
    while possibility >= 4 or possibility <= 0:                           # Loop if wrong input
        print("Add new password: 1\nSearch password:  2\nQuit program:     3")
        possibility = int(input("What do you want to do? "))
    switch_Menue(possibility)                   # Call the switch_Menue function


# Menue()     # Calls Menue function for debuging use
