import hashlib
import requests
import tkinter as tk

apiURL = "https://api.pwnedpasswords.com/range/{}"

def search():
    ### Get Password Details ###
    password = field.get()
    
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
   
    ### Displays Result ###    
    result.configure(text=str(count))


window = tk.Tk()
window.title("Password Checker")
window.geometry("400x120")

header = tk.Frame(window)
header.pack()

body = tk.Frame(window)
body.pack()

heading = tk.Label(header, text="Check to see if your passwords match any of the passwords in a large database of leaked passwords.", justify="left", wraplength=380, padx=10, pady=10)
heading.grid(row=0)

passLabel = tk.Label(body, text="Enter Password: ")
passLabel.grid(sticky="e", row=1, column=0)

field = tk.Entry(body)
field.grid(sticky="w", row=1, column=1)
field.bind("<Return>", search)

button = tk.Button(body, text="Submit", command=search)
button.grid(sticky="ew", row=1, column=2)

resultLabel = tk.Label(body, text="Number. of Appearances: ")
resultLabel.grid(sticky="e", row=2, column=0)

result = tk.Label(body)
result.grid(sticky="w", row=2, column=1)

body.grid_columnconfigure((0, 1, 2), weight=1, pad=10)
window.mainloop()


   


