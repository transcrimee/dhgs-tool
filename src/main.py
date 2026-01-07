# By transcrime
# GPL-3.0 license

print("  █████▒█    ██  ██▀███    █████▒▓█████ ▒██   ██▒")
print("▓██   ▒ ██  ▓██▒▓██ ▒ ██▒▓██   ▒ ▓█   ▀ ▒▒ █ █ ▒░")
print("▒████ ░▓██  ▒██░▓██ ░▄█ ▒▒████ ░ ▒███   ░░  █   ░")
print("░▓█▒  ░▓▓█  ░██░▒██▀▀█▄  ░▓█▒  ░ ▒▓█  ▄  ░ █ █ ▒ ")
print("░▒█░   ▒▒█████▓ ░██▓ ▒██▒░▒█░    ░▒████▒▒██▒ ▒██▒")
print(" ▒ ░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒ ░    ░░ ▒░ ░▒▒ ░ ░▓ ░")
print(" ░     ░░▒░ ░ ░   ░▒ ░ ▒░ ░       ░ ░  ░░░   ░▒ ░")
print(" ░ ░    ░░░ ░ ░   ░░   ░  ░ ░       ░    ░    ░  ")
print("          ░        ░                ░  ░ ░    ░  ")
print("Welcome to Fuefex.")
print("1.DDoS")
print("2.Hasher - MD5")
print("3.info")
print("4.Exit")
Select = input("-->")

if Select == "1":
 print("Staring DDoS Modules")
 exec(open("./modules.py").read()) # The reason why we are not using runpy because it was causing errors -- ImportError -- ModuleNotFoundError -- AttributeError
 
elif Select == "2":
 print("Staring Hasher Modules")
 exec(open("./modules hash.py").read())


elif Select == "3":
 print("Staring info Modules")
 exec(open("./info.py").read())


elif Select == "4":
 print("Exit")
 exit()

elif Select == "":
 print("Bye bye")
 exit()