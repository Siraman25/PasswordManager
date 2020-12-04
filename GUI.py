"""
Python Password Manager Framework - GUI selection system

(c) Juri Ladurner, Aris Mandolini 2020 - Python Password Manager PPM
04.12.2020
"""

import sys
import PasswordGenerator

"""
Switch Case to open the subprograms
Juri Ladurner
30.11.2020
"""


def switch_Menue(argument):
    switcher = {        # Switch-case function for python
        1: PasswordGenerator.mainPasswordGenerator(),       # Starts the password generation
        2: "",                         # TODO: enter valid options in the cases
        3: sys.exit(0)      # Program exits with code 0
    }


"""
The Menue where the user can decide with Subprograms he want to use
Juri Ladurner
30.11.2020
"""


def Menue():
    possibility = 7
    while possibility >=4 or possibility <= 0:                           # Loop if wrong input
        print("Add new password: 1\nSearch password:  2\nQuit program:     3")
        possibility = int(input("What do you want to do? "))
    switch_Menue(possibility)                   # Call the switch_Menue function


# Menue()     # Calls Menue function for testing purposes
