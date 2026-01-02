# By transcrime
# GPL-3.0 license

import platform
import psutil
import socket
import os
import sys
import subprocess
import socketserver

#print("Welcome to Fuefex.")
#print("1.DDoS")
#print("2.Hasher - MD5")
#print("3.info")
#print("4.Exit")
#Select = input("-->")

options = {"1.": "DDoS", "2.": "Hasher", "3.": "System Info", "4.": "Exit"}
print(options)
choice = input("╰─▸ ")
if "1" in choice:
    print("test")

if "2" in choice:
 repository_type = {"1.": "AUR", "2.": "Git", "3.": "Exit"}    
 print(repository_type)
 choice = input("╰─▸")
 if "1" in choice:
  repo_url = "https://aur.archlinux.org"
  print("Please add a Repository Name to Started the Git Clone")
  repository_name = input("╰─▸") 
  subprocess.run(["git", "clone", f"{repo_url}/" f"{repository_name}"])
  cd_name_getting = os.path.splitext(repository_name)[0]
  print(cd_name_getting) 
  subprocess.run(f"cd {cd_name_getting} && ls", shell=True)
  subprocess.run(["makepkg", "-is"])  
 if "2" in choice:    
  repo_url = "https://github.com"
  print("Please add Persons Github Name")
  github_name = input("╰─▸")   
  print("Please add a Repository Name to Started the Git Clone:")
  link_input = input("╰─▸")
  subprocess.run(["git", "clone", f"{repo_url}/" f"{github_name}/" f"{link_input}"])
  cd_name_getting = os.path.splitext(link_input)[0]
  print(cd_name_getting)
if "3" in choice:
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