# python script just to sync private trees for octavi os
import os
import time
import octavi

def fix (rdir_name):
  return(
    print("-----------------------------------Syncing Private repo----------------------------------------------"),
    print(),
    os.system("cd && cd " + rdir_name + " && rm -rf frameworks/base && rm -rf packages/apps/Settings && rm -rf packages/apps/OctaviLab && rm -rf packages/overlays/Themes && git clone https://github.com/Octavi-OS/maintainer_fwb.git frameworks/base && git clone https://github.com/Octavi-OS/maintainer_settings.git packages/apps/Settings && git clone https://github.com/Octavi-OS/maintainer_octavilab.git packages/apps/OctaviLab && git clone https://github.com/Octavi-OS/maintainer_themes.git packages/overlays/Themes "),
    os.system("cd && cd " + rdir_name + " && cd packages/apps/Settings/res/drawable/ && rm -rf ic_device_x00td.png "),
    os.system("cd && cd " + rdir_name + " && cd packages/apps/Settings/res/drawable/ && cp daisy.png x00td.png && cp daisy.png ic_device_x00td.png "),     
    os.system("cd && cd " + rdir_name + " && cd packages/apps/Settings/src/com/android/settings/ && rm -rf AboutPhoneData.java "),
    os.system("cp AboutPhoneData.java /home/mst/"+rdir_name+"/packages/apps/Settings/src/com/android/settings/"),
    print(),
    print("-----------------------------------Syncing Private trees---------------------------------------------"),
    print(),
    os.system("cd && cd " + rdir_name + " && git clone https://github.com/dotOS-Devices/kernel_asus_X00TD.git kernel/asus/sdm660"),
    os.system("cd && cd " + rdir_name + " && git clone https://github.com/OctaviOS-Devices/vendor_asus.git vendor/asus"),
    os.system("cd && cd " + rdir_name + " && git clone https://github.com/OctaviOS-Devices/device_asus_sdm660-common.git device/asus/sdm660-common"),
    os.system("cd && cd " + rdir_name + " && git clone https://github.com/OctaviOS-Devices/device_asus_X00TD.git device/asus/X00TD"),
    print("-----------------------------------Private Repo + Trees Synced ------------------------------------------"),
    print(),
    print("exiting................................."))
  time.sleep(2)
  os.system("clear")
  exit()
    
 
