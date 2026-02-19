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
import time
import json
import hashlib
import sys
from hmac import digest
from stylelibrary import color
from stylelibrary import style

class RepoManager:
    options = {"1": "Git", "2": "AUR", "3": "Exit"}

    def __init__(self):
        self.github_base = "https://github.com"
        self.aur_base = "https://aur.archlinux.org"
        if platform.system() == "Linux":
         try:
            # Only call this on Linux to avoid FileNotFoundError on Windows/macOS
            self.is_arch = platform.freedesktop_os_release().get("ID") == "arch"
         except (AttributeError, OSError):
            self.is_arch = False
        else:
        # On Windows or macOS, it's definitely not Arch Linux
         self.is_arch = False

    def client(self):
     try:
        while True:
          print("------------ REPOSITORY ------------")
          for key, value in self.options.items():
            print(f"{key}. {value}")
          print("------------ REPOSITORY ------------")
          choice = input("╰─▸ ")
    
          while choice not in self.options:
            print(style.bold_style(color.rgb_text(255, 0, 0, "Invalid choice. Please select a valid option.")))
            print("------------ REPOSITORY ------------")
            for key, value in self.options.items():
             print(f"{key}. {value}")
            print("------------ REPOSITORY ------------")
            choice = input("╰─▸ ")

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
      print(style.bold_style(color.rgb_text(255, 165, 0,"Please add a Repository Name to Started the Git Clone")))
      repository_name = input("╰─▸")
      if repository_name.endswith(".git"):
       subprocess.run(["git", "clone", f"{self.aur_base}/" f"{repository_name}"])
       cd_name_getting = os.path.splitext(repository_name)[0]
       print(style.bold_style(color.rgb_text(0, 255, 0, f"Successfully directory name, {cd_name_getting}")))
       if self.is_arch:
        subprocess.run(f"cd {cd_name_getting} && ls", shell=True)
       else:
          print(style.bold_style(color.rgb_text(255, 0, 0, "You're not on a Arch Linux system")))
      else:
         print(style.bold_style(color.rgb_text(255, 0, 0,"Your input is not Container .git at the end")))

class TrafficGenerator:
    options = {"1": "UPD", "2": "TCP", "3": "HTTP", "4": "Exit"}
    def client(self):
     try:
        while True:
          print("------------ ATTACK METHODS ------------")
          for key, value in self.options.items():
            print(f"{key}. {value}")
          print("------------ ATTACK METHODS ------------")
          choice = input("╰─▸ ")
          
          while choice not in self.options:
            print(style.bold_style(color.rgb_text(255, 0, 0, "Invalid choice. Please select a valid option.")))
            print("------------ ATTACK METHODS ------------")
            for key, value in self.options.items():
             print(f"{key}. {value}")
            print("------------ ATTACK METHODS ------------")
            choice = input("╰─▸ ")
          
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

class Systeminfologging:
   def __init__(self):
      self.system_path = "system.json"
      
   def logging(self):
        # System info using platform module
        print(style.bold_style(color.rgb_text( 0, 0, 255, f"System: {platform.system()}")))
        print(style.bold_style(color.rgb_text( 0, 0, 255, f"Machine: {platform.machine()}")))
        print(style.bold_style(color.rgb_text( 0, 0, 255, f"Processor: {platform.processor()}")))
        print(style.bold_style(color.rgb_text( 0, 0, 255, f"OS Version: {platform.version()}")))
        print(style.bold_style(color.rgb_text( 0, 0, 255, f"Python version: {platform.python_version()}")))

        # CPU info using psutil
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"CPU cores: {psutil.cpu_count(logical=False)}")))
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"Logical CPUs: {psutil.cpu_count(logical=True)}")))
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"CPU usage (%): {psutil.cpu_percent(interval=1)}")))

        # Memory info using psutil
        memory = psutil.virtual_memory()
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")))
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"Used Memory: {memory.used / (1024 ** 3):.2f} GB")))
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"Free Memory: {memory.free / (1024 ** 3):.2f} GB")))

        # Disk info using psutil
        disk = psutil.disk_usage('/')
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")))
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB")))
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")))

        # Network info using socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"Hostname: {hostname}")))
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"IP Address: {ip_address}")))

        # Python runtime info using sys
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"Python executable: {sys.executable}")))
        print(style.bold_style(color.rgb_text( 0, 0, 255,f"Python version: {sys.version}")))

        print(style.bold_style(color.rgb_text( 0, 0, 255,f"Platform: {sys.platform}")))

        system_info = {
          "system": platform.system(),
          "machine": platform.machine(),
          "processor": platform.processor(),
          "os_version": platform.version(),
          "python_version": platform.python_version(),
          "cpu_cores": psutil.cpu_count(logical=False),
          "logical_cpus": psutil.cpu_count(logical=True),
          "cpu_usage_percent": psutil.cpu_percent(interval=1),
          "total_memory_gb": memory.total / (1024 ** 3),
          "used_memory_gb": memory.used / (1024 ** 3),
          "free_memory_gb": memory.free / (1024 ** 3),
          "total_disk_space_gb": disk.total / (1024 ** 3),
          "used_disk_space_gb": disk.used / (1024 ** 3),
          "free_disk_space_gb": disk.free / (1024 ** 3),
          "hostname": hostname,
          "ip_address": ip_address,
          "python_executable": sys.executable,
          "python_version_detail": sys.version,
          "platform": sys.platform
         }
        with open(self.system_path, "w") as f:
         json.dump(system_info, f, indent=4)
         f.close()
         print(style.bold_style(color.rgb_text(0, 255, 0, f"System information saved to {self.system_path}")))

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
         print(style.bold_style(color.rgb_text(0, 255, 0, f"Thanks, {name}! Your username has been saved")))
         return name
        
    def change_username(self):
     if os.path.exists(self.file_name):
        os.remove(self.file_name)
        print(style.bold_style(color.rgb_text(255, 0, 0, "The previous username has been removed please add new one")))
        self.username = self.load_user()
        
class Client:
    
    def __init__(self):
        self.repo = RepoManager()
        self.networking = TrafficGenerator()
        self.security = SecurityToolkit()
        self.system_log = Systeminfologging()
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
          choice = input("╰─▸ ")

          while choice not in options:
            print(style.bold_style(color.rgb_text(255, 0, 0, "Invalid choice. Please select a valid option.")))
            print("------------ MENU ------------")
            for key, value in options.items():
             print(f"{key}. {value}")
            print("------------ MENU ------------")
            choice = input("╰─▸ ")
          if choice == "1":
               self.networking.client()
          if choice == "3":
               self.repo.client()
          if choice == "4":
             self.system_log.logging()
          if choice == "5":
               self.user_session.change_username()
          if choice == "6":
             print(style.bold_style(color.rgb_text(0, 255, 0, "Exiting Application Safely....")))
             time.sleep(1)
             print(style.bold_style(color.rgb_text(0, 255, 0, "1")))
             time.sleep(1)
             print(style.bold_style(color.rgb_text(0, 255, 0, "2")))
             time.sleep(1)
             print(style.bold_style(color.rgb_text(0, 255, 0, "3")))
             break        
        except KeyboardInterrupt:
           print(style.bold_style(color.rgb_text(255, 165, 0,"\nApplication has been Interrupted body Keyboard")))

if __name__ == "__main__": 
    application = Client()
    application.client()
