import os 
import sys

from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
assert SECRET_KEY
Fernet = Fernet(SECRET_KEY)

def encrypt_password(message):
  pass_enc = Fernet.encrypt(message.encode()).decode()
  #save the encrypted password to a file
  print("Password encrypted")
  return pass_enc

def decrypt_password(message):
  
  stored_dec_pass = Fernet.decrypt(message).decode()

  return stored_dec_pass

#encrypt_password("This is a password")

#decrypt_password()
