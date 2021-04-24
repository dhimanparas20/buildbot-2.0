# python script just to sync private trees for octavi os
import os
import time

def fix (rdir_name):
  return(
    print("-----------------------------------Syncing Private repo----------------------------------------------"),
    os.system("cd && cd " + rdir_name + " && rm -rf frameworks/base && rm -rf packages/apps/Settings && rm -rf packages/apps/OctaviLab && git clone -b 2.2 https://github.com/Octavi-Broken-Lab/frameworks_base.git frameworks/base && git clone -b 2.2 https://github.com/Octavi-Broken-Lab/android_packages_apps_Settings.git packages/apps/Settings && git clone -b 2.2 https://github.com/Octavi-Broken-Lab/android_packages_apps_OctaviLab.git packages/apps/OctaviLab "),
    os.system("cd && cd " + rdir_name + " && cd packages/apps/Settings/res/drawable/ && cp ic_device_x00td.png x00td.png "),
    os.system("cd && cd " + rdir_name + " && cd packages/apps/Settings/src/com/android/settings/ && rm -rf AboutPhoneData.java "),
    os.system("cp AboutPhoneData.java /home/mst/"+rdir_name+"/packages/apps/Settings/src/com/android/settings"),
    print("-----------------------------------Private Repo Synced ----------------------------------------------"),
    print(),
    print("exiting................................."))
  time.sleep(3)
  os.system("clear")
  exit()
    
 
