import os
import Login

if os.path.exists("UserData") is False:
    os.mkdir("UserData")
if os.path.exists("UserData/Saves") is False:
    os.mkdir("UserData/Saves")
Login.loginFunction()
