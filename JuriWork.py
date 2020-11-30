import sys

"""
Switch Case to open the Subprograms
TODO; enter valid options in the cases
"""
def switch_Menue(argument):
    switcher = {
        1: "",
        2: "",
        3: sys.exit(0)
    }


"""
The Menue where the user can add the Subprograms
"""
def Menue():
    possibility = 7
    while possibility >=4 or possibility <= 0:
        print("Add new password: 1\nSearch password:  2\nQuit program:     3")
        possibility = int(input("What do you want to do? "))
    switch_Menue(possibility)


Menue()