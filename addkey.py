# python based script to add SSH key for github so as-to sync or clone private repos.

import os
import time
import vars
import code

os.system("ssh-keygen -t ed25519 -C "+ vars.EMAIL )
print("")
print(code.VIOLET+"================================================================="+code.END)
os.system('eval "$(ssh-agent -s)" ')
print("")
print(code.VIOLET+"================================================================="+code.END)
os.system(" ssh-add ~/.ssh/id_ed25519 ")
print("")
print(code.VIOLET+"================================================================="+code.END)
print("")
print(code.RED+"Your key is saved in "+code.GREEN+'/root/.ssh/id_ed25519.pub'+code.END)
print(code.RED+"open that & file copy the key ")
print("go to github.com & login to your account")
print("goto Settings>SSH and GPG Keys >New SSH Key ")
print("Paste your key there and save it . Work done."+code.END)
print("")
print(code.VIOLET+"================================================================="+code.END)
