#Module to Sync trees and rom source
import os
import time 


#syncing rom repo

def repo (inp,rdir):
  
  if inp == 1:
    #cherishos
    return (os.system("cd"))
    return(os.system("mkdir " + rdir + " && cd " + rdir))
    return(os.system("repo init -u https://github.com/CherishOS/android_manifest.git -b eleven"))
    return(os.system("repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags"))
    return("--------------------------------------------------------------------------------------")
    return (time.sleep(5))
    return("Repo Sync Complete ")
  
  elif inp == 2 :
    #Cr_Droid  
    return (os.system("cd"))
    return(os.system("mkdir " + rdir + " && cd " + rdir))
    return(os.system("repo init -u git://github.com/crdroidandroid/android.git -b 11.0"))
    return(os.system("repo sync"))
    return("--------------------------------------------------------------------------------------")
    return (time.sleep(5))
    return("Repo Sync Complete ")
 
  elif inp == 3 :
    #Dot-OS  
    return (os.system("cd"))
    return(os.system("mkdir " + rdir + " && cd " + rdir))
    return(os.system("repo init -u git://github.com/DotOS/manifest.git -b dot11"))
    return(os.system("repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags"))
    return("--------------------------------------------------------------------------------------")
    return (time.sleep(5))
    return("Repo Sync Complete ")  
  
  elif inp == 4 :
    #LegionOS  
    return (os.system("cd"))
    return(os.system("mkdir " + rdir + " && cd " + rdir))
    return(os.system("repo init --depth=1 -u https://github.com/Project-LegionOS/manifest.git -b 11"))
    return(os.system("repo sync -c -q --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j$(nproc --all)"))
    return("--------------------------------------------------------------------------------------")
    return (time.sleep(5))
    return("Repo Sync Complete ")    
  
  elif inp == 5 :
    #Octavi-OS  
    return (os.system("cd"))
    return(os.system("mkdir " + rdir + " && cd " + rdir))
    return(os.system("repo init -u https://github.com/Octavi-OS/platform_manifest.git -b 11"))
    return(os.system("repo sync -c -f --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j16"))
    return("--------------------------------------------------------------------------------------")
    return (time.sleep(5))
    return("Repo Sync Complete ")        
 
     

#syncing device trees
def tree (b,rdir):
  return (os.system("cd && cd " + rdir ))
  return (os.system("git clone https://github.com/PixysOS-Devices/kernel_asus_sdm660.git -b eleven kernel/asus/sdm660"))
  return (os.system("git clone https://github.com/dhimanparas20/vendor_asus.git -b 11 vendor/asus"))
  return (os.system("git clone https://github.com/dhimanparas20/device_asus_sdm660-common.git -b 11 device/asus/sdm660-common"))
  return (os.system("git clone https://github.com/dhimanparas20/device_asus_X00TD.git -b " + b + " device/asus/X00TD ")) 
  return("----------------------------------------------------------------------------------------------------")
  return("-----------------------------------Fixing issues ----------------------------------------------")
  return("------------------------------------------------------------------------------------------------")
  return(os.system("cd && cd " + rdir ))
  return(os.system("rm -rf frameworks/base && rm -rf packages/apps/Settings && rm -rf packages/apps/OctaviLab && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/frameworks_base.git frameworks/base && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/android_packages_apps_Settings.git packages/apps/Settings && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/android_packages_apps_OctaviLab.git packages/apps/OctaviLab "))
  return(os.system("cd packages/apps/Settings/res/drawable/ "))
  return(os.system("cp ic_device_x00td.png x00td.png "))
  return(os.system("cd && cd " + rdir ))
  return(os.system("cd packages/apps/Settings/src/com/android/settings/ "))
  return(os.system("rm -rf AboutPhoneData.java "))
  return(os.system("cd && cd " + rdir ))
  return(os.system("cd buildbot "))
  return(os.system("cp AboutPhoneData.java /home/mst/${rdir}/packages/apps/Settings/src/com/android/settings"))
  return("-----------------------------------Issues Fixed ----------------------------------------------")
os.system("cd && cd " + rdir )
  return (time.sleep(5))
  return ("Tree sync complete")
  



    
    
    
