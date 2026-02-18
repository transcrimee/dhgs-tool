# Copyright (c) 2026 Nora Rose
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
    options = {"1": "Git", "2": "AUR", "3": "Exit"}

    def __init__(self):
        self.github_base = "https://github.com"
        self.aur_base = "https://aur.archlinux.org"


    def client(self):
     try:
        while True:
          print("------------ ATTACK METHODS ------------")
          for key, value in self.options.items():
            print(f"{key}. {value}")
          print("------------ ATTACK METHODS ------------")
          choice = input(color.rgb_text(255,105,180,"╰─▸ "))
    
          while choice not in self.options:
            print(style.bold_style(color.rgb_text(255, 0, 0, "Invalid choice. Please select a valid option.")))
            print("------------ ATTACK METHODS ------------")
            for key, value in self.options.items():
             print(f"{key}. {value}")
            print("------------ ATTACK METHODS ------------")
            choice = input(color.rgb_text(255,105,180,"╰─▸ "))

          if choice == "1":
             self.github()
          if choice == "2":
             self.aur()
          if choice == "3" : 
             break  

     except KeyboardInterrupt:
         print(style.bold_style(color.rgb_text(255, 165, 0,"\nApplication has been Interrupted body Keyboard")))

    def github(self):
       pass
    def aur(self):   
       pass

class TrafficGenerator:
    options = {"1": "UPD", "2": "TCP", "3": "HTTP", "4": "Exit"}
    def client(self):
     try:
        while True:
          print("------------ ATTACK METHODS ------------")
          for key, value in self.options.items():
            print(f"{key}. {value}")
          print("------------ ATTACK METHODS ------------")
          choice = input(color.rgb_text(255,105,180,"╰─▸ "))
          
          while choice not in self.options:
            print(style.bold_style(color.rgb_text(255, 0, 0, "Invalid choice. Please select a valid option.")))
            print("------------ ATTACK METHODS ------------")
            for key, value in self.options.items():
             print(f"{key}. {value}")
            print("------------ ATTACK METHODS ------------")
            choice = input(color.rgb_text(255,105,180,"╰─▸ "))
          
          if choice == "1":
             self.udp_flood()

          if choice == "2":
             self.udp_flood()

          if choice == "3":
             self.udp_flood() 

          if choice == "4":
             break


     except KeyboardInterrupt:
       print(style.bold_style(color.rgb_text(255, 165, 0,"\nApplication has been Interrupted body Keyboard")))
    def  udp_flood(self):
        print("123")


class SecurityToolkit:
    pass

class SessionManager:
    def __init__(self):
       self.file_name = "username.json"
       self.username = self.load_user()

    def load_user(self):
     if os.path.exists(self.file_name):
       with open(self.file_name, "r") as f:
           data = json.load(f)
           self.username = data.get("username", "User")
     else:
        name = input("Enter your username:")
        while name == "":
          print("It seems that your username was empty please re-enter it!")
          name = input("Enter your username:")  
        with open(self.file_name, "w") as f: # Creates the username.json and ready to writes the username into it 
         json.dump({"username": name}, f) # Dumps the username into the json file
         print(f"Thanks, {name}! Your username has been saved")
         return name
        
    def change_username():
       pass
         
class Client:
    
    def __init__(self):
        self.repo = RepoManager()
        self.networking = TrafficGenerator()
        self.security = SecurityToolkit()
        self.user_session = SessionManager()

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
          if choice == "1":
               self.networking.client()
          if choice == "3":
               self.repo.client()
        except KeyboardInterrupt:
           print(style.bold_style(color.rgb_text(255, 165, 0,"\nApplication has been Interrupted body Keyboard")))

if __name__ == "__main__": 
    application = Client()
    application.client()
