def PasswordGeneration(numsel, charsel, length):
    if numsel is False and charsel is False:
        minNumber1 = 65
        maxNumber1 = 91
        minNumber2 = 97
        maxNumber2 = 123
        numAmount = 2
    elif numsel is False and charsel is True:
        minNumber1 = 33
        maxNumber1 = 48
        minNumber2 = 58
        maxNumber2 = 127
        numAmount = 2
    elif numsel is True and charsel is False:
        minNumber1 = 48
        maxNumber1 = 58
        minNumber2 = 65
        maxNumber2 = 91
        minNumber3 = 97
        maxNumber3 = 123
        numAmount = 3
    elif numsel is True and charsel is True:
        minNumber1 = 33
        maxNumber1 = 127
        numAmount = 1

    if numAmount == 3:
        finallist = [*range(minNumber1, maxNumber1)] + [*range(minNumber2, maxNumber2)] + [*range(minNumber3, maxNumber3)]
    elif numAmount == 2:
        finallist = [*range(minNumber1, maxNumber1)] + [*range(minNumber2, maxNumber2)]
    else:
        finallist = [*range(minNumber1, maxNumber1)]
    print(finallist)


webSiteName = input("Write a name for your website: ")
webSiteUrl = input("Write the url of the website: ")
numberSelector = input("Do you want to use numbers (default [RETURN]: yes)/no)? ")
specCharSelector = input("Do you want to use special characters (default [RETURN]: yes)/no)? ")
passwordLength = int(input("How long do you want your password to be? "))
print()
print("Thank you. We are generating your password.")
if numberSelector.lower() == "" or numberSelector.lower() == "yes" or numberSelector.lower() == "y":
    numberSelector = True
else:
    numberSelector = False

if specCharSelector.lower() == "" or specCharSelector.lower() == "yes" or specCharSelector.lower() == "y":
    specCharSelector = True
else:
    specCharSelector = False

PasswordGeneration(numberSelector, specCharSelector, passwordLength)
