#Module to Sync trees and rom source
import os
import time 


#syncing rom repo

def repo (inp,rdir):
  
  if inp == 1:
    #cherishos
    return
    (  
    os.system("cd && mkdir "+ rdir + " && cd " + rdir + " && repo init -u https://github.com/CherishOS/android_manifest.git -b eleven"),
    os.system("repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags"),
    print("--------------------------------------------------------------------------------------"),
    time.sleep(5),
    print("Repo Sync Complete ")
    )
  
  elif inp == 2 :
    #Cr_Droid  
    return
    (
    os.system("cd && mkdir "+ rdir + " && cd " + rdir + " && repo init -u git://github.com/crdroidandroid/android.git -b 11.0"),
    os.system("repo sync"),
    print("--------------------------------------------------------------------------------------"),
    time.sleep(5),
    print("Repo Sync Complete ")
    )
 
  elif inp == 3 :
    #Dot-OS  
    return
    (
    os.system("cd && mkdir "+ rdir + " && cd " + rdir + " && repo init -u git://github.com/DotOS/manifest.git -b dot11"),
    os.system("repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags"),
    print("--------------------------------------------------------------------------------------"),
    time.sleep(5),
    print("Repo Sync Complete ")  
    )
  
  elif inp == 4 :
    #LegionOS  
    return
    (
    os.system("cd && mkdir "+ rdir + " && cd " + rdir + " && repo init --depth=1 -u https://github.com/Project-LegionOS/manifest.git -b 11"),
    os.system("repo sync -c -q --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j$(nproc --all)"),
    print("--------------------------------------------------------------------------------------"),
    time.sleep(5),
    print("Repo Sync Complete "),    
    )
  
  elif inp == 5 :
    #Octavi-OS
    return
    (    
    os.system("cd && mkdir "+ rdir + " && cd " + rdir + " && repo init -u https://github.com/Octavi-OS/platform_manifest.git -b 11"),
    os.system("repo sync -c -f --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j16"),
    print("--------------------------------------------------------------------------------------"),
    time.sleep(5),
    print("Repo Sync Complete ")        
    )
 
     

#syncing device trees
def tree (b,rdir):
  return
  (
  os.system("cd && cd " + rdir + " && git clone https://github.com/PixysOS-Devices/kernel_asus_sdm660.git -b eleven kernel/asus/sdm660"),
  os.system("git clone https://github.com/dhimanparas20/vendor_asus.git -b 11 vendor/asus"),
  os.system("git clone https://github.com/dhimanparas20/device_asus_sdm660-common.git -b 11 device/asus/sdm660-common"),
  os.system("git clone https://github.com/dhimanparas20/device_asus_X00TD.git -b " + b + " device/asus/X00TD "),
  print("----------------------------------------------------------------------------------------------------"),
  print("-----------------------------------Fixing issues ----------------------------------------------"),
  print("------------------------------------------------------------------------------------------------")
  )
  
  



    
    
    
