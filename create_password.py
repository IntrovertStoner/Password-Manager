import os 
import sys
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from encrypt import encrypt_password
from tkinter import messagebox

def create_password(website_entry, login_entry, password_entry, add_password_window):
  website = website_entry.get()
  login = login_entry.get()
  password = password_entry.get()
  #print(password)
  password = encrypt_password(password)
  #print(password)
  with open("passwords.csv", mode="a+",newline="") as file:
      file.write(f"{password},{website},{login}\n")


  #create a message box saying the password was successfully saved
  messagebox.showinfo(title="Password Saved", message="Password saved successfully.")

  #destroy the window after the password is saved
  add_password_window.destroy()





