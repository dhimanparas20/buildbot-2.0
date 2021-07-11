# place all your variables here 
# This is the only file you need to edit 
# Fill the details between the quotes

import os
import time

# Name of server
SERVER_NAME = "ubuntu"  #change according to your server name

# Github
EMAIL = ""  # your github email address
USER_NAME = "" # your github username

# Names of roms to sync
ROM_NAME1 = "CherishOS"  # rom 1 name 
ROM_NAME2 = "Cr-Droid"  #rom 3 name
ROM_NAME3 = "DotOS"  #rom 3 name
ROM_NAME4 = "Octavi OS"  #rom 4 name 

# Repo init commands of the roms
ROM_LINK1 = "repo init -u https://github.com/CherishOS/android_manifest.git -b eleven && repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags "
ROM_LINK2 = "repo init -u git://github.com/crdroidandroid/android.git -b 11.0 && repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags"
ROM_LINK3 = "repo init -u git://github.com/DotOS/manifest.git -b dot11 && repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags"
ROM_LINK4 = "repo init -u https://github.com/Octavi-OS/platform_manifest.git -b 11 && repo sync -c -f --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j16"

# Links for the trees 
# Branch will be automatically asked evertime inside script so no need to worry
DT = "" # device tree
CDT = ""  # keep empty if you dont have any commmon tree else put common tree link
VT = ""  # vendor tree
KT = ""  # kernel tree

# Place where you want trees to be synced 
P_DT = "device/asus/X00TD"
P_CDT = ""
P_VT = ""
P_KT = ""

# Name of SourceForge diractory
SF = "mst-2069@frs.sourceforge.net:/home/frs/project/" # needed to upload to sourceforge 

# Name of rclone cloud
RC = "gd:" # needed to upload to google drive using rclone

# Name of output Directory
OUT = "out/target/product/X00TD"  # where the rom zip is placed after rom getting compiled sucessfully

# ===============================DO NOT EDIT AFTER THIS==================================#
print("===============SAVING GITHUB INFO===========")
os.system ("git config --global user.email \"" +EMAIL+ "\" && git config --global user.name \"" +USER_NAME+ "\"")
