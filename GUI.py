from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os 
import sys
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pkg_resources

#Folder containing the functions
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'funcs'))
if module_path not in sys.path:
    sys.path.append(module_path)

# Path for the csv file and img folder
csv_path = pkg_resources.resource_filename(__name__, 'passwords.csv')
image_path = pkg_resources.resource_filename(__name__, 'pics')

# Import the functions from my files
from create_password import create_password
from encrypt import decrypt_password, encrypt_password
from search import search_password
from delete_password import delete_password
from install_requirements import install_requirements





# Basic configs for the GUI
root = Tk()
root.resizable(0, 0)
root.geometry("500x500")
root.title("Password Manager")
#Variable for the icon image
icon_photo = Image.open(os.path.join(image_path,"backup.ico"))
icon_photo = ImageTk.PhotoImage(icon_photo)
root.iconphoto(False, icon_photo)
# Make the GUI open in the middle of the screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Variable for the search photo
original_image = Image.open(os.path.join(image_path,"search.png"))
resized_image = original_image.resize((15, 15), Image.LANCZOS)
search_image = ImageTk.PhotoImage(resized_image)


# Function to update the Treeview after adding a new password
def update_treeview():
    tree.delete(*tree.get_children())
    with open("passwords.csv", "r") as f:
        for line in f:
            password, website, username = line.strip().split(",")
            tree.insert("", "end", values=(website, username, password))

# Create a box for a search bar
search_box = Frame(root)
search_box.pack(side=TOP, fill=X)

# Create a label for the search bar
search_label = Label(search_box, text="Search:")
search_label.pack(side=LEFT, padx=5, pady=5)

# Create an entry for the search bar
search_entry = Entry(search_box)
search_entry.pack(side=LEFT, padx=5, pady=5)

# Create a button for the search bar
search_button = Button(search_box, image=search_image, compound=LEFT, command=lambda: search_password(search_entry, password_box, tree))
search_button.pack(side=LEFT, padx=5, pady=5)

# Create a button to clear the search bar
clear_button = Button(search_box, text="Clear", command=update_treeview)
clear_button.pack(side=LEFT, padx=5, pady=5)

# Function to handle multiple commands
def save_and_update(website_entry, login_entry, password_entry, window):
    create_password(website_entry, login_entry, password_entry, window)
    update_treeview()

# Function to open a new window for editing the selected password
def open_edit_password_window():
    selected_item, website, username, password = on_tree_select()  # Get the selected item and its values

    edit_password_window = Toplevel(root)
    edit_password_window.geometry("300x240")

    Label(edit_password_window, text="Website:").pack(pady=5)
    website_entry = Entry(edit_password_window)
    website_entry.pack(pady=5)
    
    Label(edit_password_window, text="Username:").pack(pady=5)
    login_entry = Entry(edit_password_window)
    login_entry.pack(pady=5)
    
    Label(edit_password_window, text="Password:").pack(pady=5, padx=30)
    password_entry = Entry(edit_password_window, show="*")
    password_entry.pack(pady=5)
    
    Button(edit_password_window, text="Update to file", command=lambda: save_edited_password(website_entry, login_entry, password_entry, edit_password_window)).pack(pady=10)

    # Set the values of the selected item in the entries
    website_entry.insert(0, website)
    login_entry.insert(0, username)
    password_entry.insert(0, password)

# Function to save the edited password to the csv file
def save_edited_password(website_entry, login_entry, password_entry, window):
    selected_item, website, username, password = on_tree_select()  # Get the selected item and its values
    new_website = website_entry.get()
    new_username = login_entry.get()
    new_password = password_entry.get()
    new_password_enc = encrypt_password(new_password)

    selected_item_index = tree.index(selected_item)  # Get the index of the selected item

    # Read the file and update the corresponding line
    lines = []
    with open("passwords.csv", "r") as file:
        lines = file.readlines()

        for conta in lines:
            conta_index = lines.index(conta)
            if conta_index == selected_item_index:
                lines[conta_index] = new_password_enc + "," + new_website + "," + new_username + "\n"

    with open("passwords.csv", "w") as file:
        for line in lines:
            file.write(line)

    messagebox.showinfo(title="Password Saved", message="Password saved successfully.")
    update_treeview()
    window.destroy()

# Function to open a new window for adding a password
def open_add_password_window():
    add_password_window = Toplevel(root)
    add_password_window.title("Add Password")
    add_password_window.geometry("300x240")

    Label(add_password_window, text="Website:").pack(pady=5)
    website_entry = Entry(add_password_window)
    website_entry.pack(pady=5)
    
    Label(add_password_window, text="Username:").pack(pady=5)
    login_entry = Entry(add_password_window)
    login_entry.pack(pady=5)
    
    Label(add_password_window, text="Password:").pack(pady=5, padx=30)
    password_entry = Entry(add_password_window, show="*")
    password_entry.pack(pady=5)
    
    Button(add_password_window, text="Save to file", command=lambda: save_and_update(website_entry, login_entry, password_entry, add_password_window)).pack(pady=10)

# Selection event
def on_tree_select(event=None):
    selected_item = tree.selection()[0]  # Get the selected item
    values = tree.item(selected_item, "values")  # Get the values of the selected item
    website_selected = values[0]  # Extract the website (assuming it's the first column)
    username_selected = values[1]  # Extract the username (assuming it's the second column)
    password_selected = values[2]  # Extract the password (assuming it's the third column)
    return selected_item, website_selected, username_selected, password_selected

# Function to update the table with the decrypted password on the selected field
def update_table():
    selected_item, website, username, password = on_tree_select()  # Get the selected item and password
    decrypted_password = decrypt_password(password)  # Decrypt the password
    tree.set(selected_item, "Password", decrypted_password)

# Create a box for 4 buttons
button_box = Frame(root)
button_box.pack(side=TOP, fill=X)

# Create the buttons for the box and grid them
decrypt_button = Button(button_box, text="Decrypt", command=update_table, bg="lightgreen", fg="black")
decrypt_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

add_password_button = Button(button_box, text="Add Password", command=open_add_password_window, bg="lightyellow", fg="black")
add_password_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

delete_password_button = Button(button_box, text="Delete Password", command=lambda: delete_password(tree, on_tree_select()[0]), bg="lightcoral", fg="black")
delete_password_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

edit_password_button = Button(button_box, text="Edit Password", command=open_edit_password_window, bg="lightgrey", fg="black")
edit_password_button.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

# Configure the grid columns to have equal weight
button_box.grid_columnconfigure(0, weight=1)
button_box.grid_columnconfigure(1, weight=1)
button_box.grid_columnconfigure(2, weight=1)
button_box.grid_columnconfigure(3, weight=1)

# Create a box for the password list to be shown from the csv file
password_box = Frame(root)
password_box.pack(side=TOP, fill=BOTH, expand=True)

# Create a Treeview widget with 3 columns
tree = ttk.Treeview(password_box, columns=("Website", "Username", "Password"), show="headings")
tree.heading("Website", text="Website")
tree.heading("Username", text="Username")
tree.heading("Password", text="Password")

# Configure the columns
tree.column("Website", anchor=CENTER, width=100)
tree.column("Username", anchor=CENTER, width=100)
tree.column("Password", anchor=CENTER, width=100)

# For each line in the csv file, add it to the Treeview
with open("passwords.csv", "r") as f:
    for line in f:
        password, website, username = line.strip().split(",")
        tree.insert("", "end", values=(website, username, password))

# Add the Treeview widget to the password_box
tree.pack(side=LEFT, fill=BOTH, expand=True)

# Create a scrollbar for the Treeview
password_scroll = Scrollbar(password_box, orient=VERTICAL, command=tree.yview)
password_scroll.pack(side=RIGHT, fill=Y)
tree.configure(yscrollcommand=password_scroll.set)

# Bind the selection event to the on_tree_select function
tree.bind("<<TreeviewSelect>>", on_tree_select)

root.mainloop()