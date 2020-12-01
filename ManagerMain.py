from random import randint      # import random function

# TODONE: Start Menu with "GUI"
# TODO: Special chars Selector (ON/OFF)
# TODO: Numbers Selector (ON/OFF)
# TODONE: User login system
# TODO: Encryptor/Decryptor system
# TODO: General Password manager System

"""
Please note: this document serves for PROTOTYPING purposes only. It is not the final product.

(c) Aris Mandolini 2020 - Python Password Manager PPM
24.11.2020
"""

charNumber = 10000000000000000000      # arbitrary length number of password characters

ASCIIkey = []       # array initialization (storage of ASCII chars in DEC)

for i in range(0, charNumber, 1):       # loop to fill array from location 0 to charNumber-1
    ASCIIkey.append(randint(32, 126))

generatedPassword = "".join(chr(j) for j in ASCIIkey)       # conversion ASCII-DEC to CHAR and stringing CHARs together


# print(ASCIIkey)
print(generatedPassword)
