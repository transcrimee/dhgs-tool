# Copyright (c) 2026 Your Name
# Licensed under MIT License

import platform
import psutil
import socket
import os
import sys
import subprocess
import socketserver
import threading
import requests
import random
import sys
import json
import hashlib
from hmac import digest
from stylelibrary import color
from stylelibrary import style

class RepoManager:
    pass

class TrafficGenerator:
    pass

class SecurityToolkit:
    pass

class SessionManager:
    file_name = "username.json"
    if os.path.exists(file_name):
       with open(file_name, "r") as f:
           data = json.load(f)
           username = data.get("username", "")
    else:
        username = input("Enter your username:")
        while username == "":
          print("It seems that your username was empty please re-enter it!")
          username = input("Enter your username:")  
        with open(file_name, "w") as f: # Creates the username.json and ready to writes the username into it 
         json.dump({"username": username}, f) # Dumps the username into the json file
         print(f"Thanks, {username}! Your username has been saved")

class Client:
    
    def __init__(self):
        self.repo = RepoManager
        self.networking = TrafficGenerator
        self.security = SecurityToolkit
        self.user_session = SessionManager

    def client(self):
        options = {"1": "DDoS", "2": "Hasher", "3": "Git", "4": "System Info", "5": "Change Username", "6": "Exit"}

        try:
         while True:
          print(f"Welcome back, {self.user_session.username}")
          print("------------ MENU ------------")
          for key, value in options.items():
            print(f"{key}. {value}")
          print("------------ MENU ------------")
          choice = input(color.rgb_text(255,105,180,"╰─▸ "))

          while choice not in options:
            print(style.bold_style(color.rgb_text(255, 0, 0, "Invalid choice. Please select a valid option.")))
            print("------------ MENU ------------")
            for key, value in options.items():
             print(f"{key}. {value}")
            print("------------ MENU ------------")
            choice = input(color.rgb_text(255,105,180,"╰─▸ "))

        except KeyboardInterrupt:
           print(style.bold_style(color.rgb_text(255, 165, 0,"\nApplication has been Interrupted body Keyboard")))

if __name__ == "__main__": 
    application = Client()
    application.client()
