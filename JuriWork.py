import sys

"""
Switch Case to open the Subprograms
Juri Ladurner
30.11.2020

"""
def switch_Menue(argument):
    switcher = {
        1: "",                         # TODO; enter valid options in the cases
        2: "",                         # TODO; enter valid options in the cases
        3: sys.exit(0)
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
    switch_Menue(possibility)                   # Open the "switch_Menue" function


Menue()