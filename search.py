from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os 
import sys
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from tkinter import PhotoImage
from PIL import Image, ImageTk


def search_password(search_entry,password_box,tree):
  search_entry_text = search_entry.get()
  #print("searched:",search_entry_text)
  index_found=[]
  with open("passwords.csv", "r") as f:
    lines = f.readlines()
    #print("lines:",lines)
    #get the index of the line im at
    for index, line in enumerate(lines):
      password,website,username = line.strip().split(",")
      print("website:",website)
      if search_entry_text in website:
        index_found.append(index)
        print("index found:",index)
    
      
  
  # Clear the Treeview widget
  tree.delete(*tree.get_children())

  #Open the text to find the index of the accounts found and add them to the treeview
  with open("passwords.csv", "r") as f:
    lines = f.readlines()
    password, website, username = line.strip().split(",")
    for index, data in enumerate(lines):
      #print("index:",index)
    
      if index in index_found:
        password, website, username = data.strip().split(",")
        tree.insert("", "end", values=(website, username, password))



      # Add the Treeview widget to the password_box


        


