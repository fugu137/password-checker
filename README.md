# Password Checker
This python script allows users to check if their passwords match any of the passwords in a database of passwords obtained via data breaches. The script uses the API at https://haveibeenpwned.com/Passwords and makes it possible to check passwords without inputting them into the password field on the website. (Some users may be reluctant to do this, as they may fear their password being compromised in the process.) The script hashes each password and then sends only the first five characters to the pwnedpassword service. The service returns all hashed passwords in the database which start with the same five characters (~500 entries), and this script searches these entries to see if any match the user's password. In this way, the pwnedpassword service never has access to the user's password (even in hashed form), and never knows whether it appears in the database.

## Instructions For Use:
1. Download `password_checker.py` from the repository.
2. Download the appropriate version of Python at https://www.python.org/downloads/ and follow the instructions at https://wiki.python.org/moin/BeginnersGuide/Download to install it (unless you already have it).
3. Open the Command Prompt/Terminal and navigate to the folder whether you saved `password_checker.py`. 
4. Next, type, `python3 -m pip install requests`. (This installs the module used to communicate with the pwnedpassword service.)
5. After the requests module is installed type, `python3 password_checker.py`. The script should run and give you a prompt to type in a password. You can check as many passwords as you like.
