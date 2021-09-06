from tkinter import * 
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
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
    if website == "" or email == "":
        messagebox.showinfo(title="Oops", message="no website or email is added")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nis it ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                websiteE.delete(0, END)
                passwordE.delete(0, END)

        if website == "":
            messagebox.askokcancel(title=website, message="no website is added")
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
websiteE = Entry(width = 35)
websiteE.grid(row= 1, column= 1, columnspan = 2)

emailE = Entry(width = 35)
emailE.grid(row= 2, column= 1, columnspan = 2)
emailE.insert(0,"salehabadimelika@gmail.com")

passwordE = Entry(width = 21)
passwordE.grid(row= 3, column= 1)

# Buttons
passwordB = Button(text= "Generate Password", command = generate_pass)
passwordB.grid(row= 3, column= 2)
addB = Button(text="Add",width=35, command = save)
addB.grid(row= 4, column= 1, columnspan = 2)



window.mainloop()
