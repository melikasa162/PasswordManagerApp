from tkinter import * 
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letter +password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    passwordE.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = websiteE.get()
    email = emailE.get()
    password = passwordE.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or email == "":
        messagebox.showinfo(title="Oops", message="no website or email is added")
    else:
        try:
            with open("data.json","r") as data_file:
                # read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update old data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # save updated data
                json.dump(data, data_file, indent= 4)
        finally:
            websiteE.delete(0, END)
            passwordE.delete(0, END)

# ---------------------------- Find Password ----------------------------- #
def find_password():
    website = websiteE.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title= website, message= f"{email}\npassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ----------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady=50)

# Canvas
canvas = Canvas(width= 200, height =200)
canvas.grid(row= 0, column= 1)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100 , image= image)

# Labels
websiteL = Label(text="Website:")
websiteL.grid(row= 1, column=0)
websiteL.focus()
EmailL = Label(text="Email/Username")
EmailL.grid(row= 2, column= 0)

passwordL = Label(text="Password:")
passwordL.grid(row= 3, column= 0)

# Entries
websiteE = Entry(width = 21)
websiteE.grid(row= 1, column= 1)

emailE = Entry(width = 35)
emailE.grid(row= 2, column= 1, columnspan = 2)
emailE.insert(0,"salehabadimelika@gmail.com")

passwordE = Entry(width = 21)
passwordE.grid(row= 3, column= 1)

# Buttons
searchB = Button(text= "search", width=13, command = find_password)
searchB.grid(row= 1, column =2)
passwordB = Button(text= "Generate Password", command = generate_pass)
passwordB.grid(row= 3, column= 2)
addB = Button(text="Add",width=35, command = save)
addB.grid(row= 4, column= 1, columnspan = 2)



window.mainloop()
