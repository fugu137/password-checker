import hashlib
import requests

print("", end="\n")
print("=========== PASSWORD CHECKER ===========")
print("")
print("Check if your passwords are the same as any of the passwords exposed in past data breaches.")
print("(If they are, you probably want to change them, since hackers are likely to try these passwords when attempting to hack into your accounts.)")
print(">>> Uses the password database and API from https://haveibeenpwned.com/Passwords <<<")

while True:
    print()

    ### Get Password Details ###
    password = input("\u001b[32m" + "Enter a password: " + "\033[0m")
    apiURL = "https://api.pwnedpasswords.com/range/{}"

    passwordHash = hashlib.sha1(password.encode()).hexdigest()
    prefix = passwordHash[0:5]
    suffix = passwordHash[5:]

    ### Make HTTP Request and Decode Response ###
    encoding = "UTF-8"
    response = requests.get(apiURL.format(prefix))
    suffixList = response.content.decode(encoding).split("\r\n")

    ### Check if Suffix is in suffixList and Print Count ###
    count = 0

    for s in suffixList:
        split = s.split(":") # Divides each entry into suffix (left of the colon) and count (right of the colon)
        comparisonSuffix = split[0]  
        numberOfAppearances = int(split[1])

        if comparisonSuffix.lower() == suffix.lower():
            count = numberOfAppearances
            break
   
    ### Changes Color of the Count Depending on Whether the Password was Found in the Database ###
    countStr = str(count)
    if count > 0:
        countStr = "\u001b[31m" + countStr + "\033[0m"
    elif count == 0:
        countStr = "\u001b[32m" + countStr + "\033[0m"

    ### Prints Result ###    
    print("Number of times your password appears in the database: " + countStr)


