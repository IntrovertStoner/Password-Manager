import os
import sys
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from encrypt import *
from tkinter import messagebox

# Function to delete password from the csv file and update the treeview
def delete_password(tree, selected_item):
    # Get the values of the selected item
    values = tree.item(selected_item, "values")
    website = values[0]
    username = values[1]

    # Remove the selected item from the Treeview
    tree.delete(selected_item)

    # Read the file and remove the corresponding line
    lines = []
    with open("passwords.csv", "r") as file:
        lines = file.readlines()

    with open("passwords.csv", "w") as file:
        for line in lines:
            password_csv, website_csv, username_csv = line.strip().split(",")
            if website != website_csv or username != username_csv:
                file.write(line)

    messagebox.showinfo(title="Password Deleted", message="Password deleted successfully.")