from encrypt import encrypt_password
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os 
import sys
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from tkinter import PhotoImage
from PIL import Image, ImageTk


def create_password(website_entry, username_entry, password_entry):
  website = website_entry.get()
  username = username_entry.get()
  password = password_entry.get()
  encrypted_password = encrypt_password(password)
  with open("passwords.csv", "a") as f:
      f.write(f"{encrypt_password}, {website}, {username}\n")
  website_entry.delete(0, END)
  username_entry.delete(0, END)
  password_entry.delete(0, END)