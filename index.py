import subprocess
print("Hello Welcome to my app")
print("here in this you can open apps by searching for them, for now you can open only some apps, they are:")
print("1. Command prompt")
print("2. Calculator")
print("3. Whatsapp")
print("4. Google ")
print("To open apps from the above list type the name of the app")
open_app = str(input("Please Enter the app name here-"))
if(open_app == str("Command prompt")):
    subprocess.call('cmd.exe')
if(open_app == str("Calculator")):
    subprocess.call('calc.exe')
if(open_app == str("Whatsapp")):
    subprocess.call('C:/Users/Turpu Shriniketan Ra/AppData/Local/WhatsApp/WhatsApp.exe')
if(open_app == str("goo")):
    subprocess.call('C:/Program Files/Google/Chrome/Application/chrome.exe')    
