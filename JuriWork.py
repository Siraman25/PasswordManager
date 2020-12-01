import Login

"""
Make the Settings so the user can day if he want to stay logged in
Juri Ladurner
1.12.2020
"""
def LoginSettingStayLogin():
    ReadFile = open("UserData/" + Login.username.lower() + ".txt", "r")
    ReadFifthLine= ReadFile.readlines()[3]

    if ReadFifthLine == "€stayLoggedIn = true":
        print("Not finished")        # TODO: The user must stay logged in
    elif ReadFifthLine == "€stayLoggedIn = false":
        print("Not finished")       # TODO: The user must logged out
    else:
        print("Error: File not Found or the Text in it was changed")
