"""
Python Password Manager Framework - Startup checks system

(c) Aris Mandolini 2020 - Python Password Manager PPM
04.12.2020
"""

import os
import Login

if os.path.exists("UserData") is False:
    os.mkdir("UserData")
if os.path.exists("UserData/Saves") is False:
    os.mkdir("UserData/Saves")
Login.loginFunction()
