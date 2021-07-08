# place all your variables here 
# This is the only file you need to edit 
# if you dont want to edit this you can also run "python3 entvar.py" to add variables by script

# Name of server
SERVER_NAME = "mst"

# Names of roms to sync
ROM_NAME1 = "CherishOS"
ROM_NAME2 = "Cr-Droid"
ROM_NAME3 = "DotOS"
ROM_NAME4 = "Octavi OS"

# Repo init commands of the roms
ROM_LINK1 = "repo init -u https://github.com/CherishOS/android_manifest.git -b eleven && repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags "
ROM_LINK2 = "repo init -u git://github.com/crdroidandroid/android.git -b 11.0 && repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags"
ROM_LINK3 = "repo init -u git://github.com/DotOS/manifest.git -b dot11 && repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags"
ROM_LINK4 = "repo init -u https://github.com/Octavi-OS/platform_manifest.git -b 11 && repo sync -c -f --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j16"

# Links for the trees 
# Branch will be automatically asked evertime inside script so no need to worry
DT = "https://github.com/dhimanparas20/device-asus-X00TD.git" # device tree
CDT = "https://github.com/dhimanparas20/device_asus_sdm660-common.git"  # keep empty if you dont have any commmon tree
VT = "https://github.com/dhimanparas20/vendor-asus.git"  # vendor tree
KT = "https://github.com/dotOS-Devices/kernel_asus_X00TD.git"  # kernel tree

# PLce where you want trees to be synced
P_DT = "device/asus/X00TD"
P_CDT = "device/asus/sdm660-common"
P_VT = "vendor/asus"
P_KT = "kernel/asus/sdm660"

# Name of SourceForge Project
SF = "mst-2069@frs.sourceforge.net:/home/frs/project/" # needed to upload to sourceforge 

# Name of rclone cloud
RC = "gd:" # needed to upload to google drive using rclone

# Name of output Directory
OUT = "out/target/product/X00TD"  # where the rom zip is placed after rom getting compiled sucessfully
