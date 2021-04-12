import hashlib
import requests
import tkinter as tk

apiURL = "https://api.pwnedpasswords.com/range/{}"

def search(event):
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


def toggleMaskPassword():
    if checkbuttonValue.get():
        field.configure(show="")
    else:
        field.configure(show="*")

### Build GUI ###
window = tk.Tk()
window.title("Password Checker")
window.geometry("400x150")

checkbuttonValue = tk.BooleanVar()

header = tk.Frame(window)
header.pack()

body = tk.Frame(window)
body.grid_columnconfigure((0, 1, 2), weight=1, pad=10)
body.pack()

heading = tk.Label(header, text="Check to see if your passwords match any of the passwords in a large (~600 million) database of leaked passwords.", justify="left", wraplength=380, padx=10, pady=10)
heading.pack()

passLabel = tk.Label(body, text="Enter Password: ")
passLabel.grid(sticky="e", row=0, column=0)

field = tk.Entry(body, show="*")
field.grid(sticky="w", row=0, column=1)
field.bind("<Return>", search)

button = tk.Button(body, text="Submit")
button.grid(sticky="w", row=0, column=2)
button.bind("<Button-1>", search)

checkbox = tk.Checkbutton(body, text="Show password", var=checkbuttonValue, command=toggleMaskPassword)
checkbox.grid(sticky="w", row=1, column=1)

resultLabel = tk.Label(body, text="No. of Appearances: ")
resultLabel.grid(sticky="e", row=2, column=0)

result = tk.Label(body, pady=5)
result.grid(sticky="w", row=2, column=1)

window.mainloop()


   


