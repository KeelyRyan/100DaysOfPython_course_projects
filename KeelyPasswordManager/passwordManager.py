from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for char in range(0, 10)]
    password_list += [choice(symbols) for sym in range(2, 4)]
    password_list += [choice(numbers) for num in range(2, 4)]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    username = username_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {website:
                    {"username": username,
                     "password": password
                     }
                }
    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Missing Data", message=f"You've left some fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
                # updating data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # writing new data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- Search Password ------------------------ #
def search_data():
    username = username_entry.get()
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            # reading old data
            data = json.load(data_file)
            password = data[website]["password"]
            if username == data[website]["username"]:
                messagebox.showinfo(title=f"{website} Information", message=f"{username} \n {password}")
                pyperclip.copy(password)
    except KeyError:
        messagebox.showinfo(title=f"{website} Information", message="Website and/or Email/Username is incorrect")
    except FileNotFoundError:
        messagebox.showinfo(title=f"{website} Information", message="No data file exists.")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()
search_button = Button(text="Search", command=search_data, width=14)
search_button.grid(row=1, column=2, sticky="w")

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky="e")
username_entry = Entry(width=53)
username_entry.grid(row=2, column=1, columnspan=2, sticky="w")
username_entry.insert(0, "")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="w")

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=45, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
