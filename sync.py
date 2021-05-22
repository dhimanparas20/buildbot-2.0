#Module to Sync trees and rom source
import os
import time 

#display input for rom sync
#displays the choices 
def disp():
  return(
    print(),
    print ("------------------------------------------------"),
    print ("            Choose rom Choice to sync           "),
    print ("------------------------------------------------"),
    print ("1: CherishOS"),
    print ("2: Cr-Droid "),
    print ("3: DotOS "),
    print ("4: Octavi OS"),
    print ("=================================================="))
    
    
    
def opt () :
  return(
    print(),
    print ("------------------------------------------------"),
    print ("            Choose rom Choice to compile        "),
    print ("------------------------------------------------"),
    print ("1: CherishOS"),
    print ("2: Cr-Droid "),
    print ("3: DotOS "),
    print ("4: Octavi OS"),
    print("=================================================="))    

#syncing rom repo
def repo (inp,rdir):
  
  if inp == 1:
    #cherishos
    return(
      os.system("cd && mkdir "+ rdir + " && cd " + rdir + " && repo init -u https://github.com/CherishOS/android_manifest.git -b eleven"),
      os.system("cd  && cd " + rdir + " && repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags"),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print("Repo Sync Complete "))
    
  
  elif inp == 2 :
    #Cr_Droid  
    return(
      os.system("cd && mkdir "+ rdir + " && cd " + rdir + " && repo init -u git://github.com/crdroidandroid/android.git -b 11.0"),
      os.system("cd  && cd " + rdir + " && repo sync"),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print("Repo Sync Complete "))
    
 
  elif inp == 3 :
    #Dot-OS  
    return(
      os.system("cd && mkdir "+ rdir + " && cd " + rdir + " && repo init -u git://github.com/DotOS/manifest.git -b dot11"),
      os.system("cd  && cd " + rdir + " && repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags"),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print("Repo Sync Complete "))
      
  
  elif inp == 4 :
    #Octavi-OS
    return(
      os.system("cd && mkdir "+ rdir + " && cd " + rdir + " && repo init -u https://github.com/Octavi-OS/platform_manifest.git -b 11"),
      os.system("cd  && cd " + rdir + " && repo sync -c -f --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j16"),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print("Repo Sync Complete "))       
    
 
     

#syncing device trees
def tree (opt,b,rdir):
  if opt == 'N' or opt == 'n':
    return(
      print("/////////////////////////////===CLONING OLD TREES===////////////////////////////////////"),
      os.system("cd && cd " + rdir + " && git clone https://github.com/ElectroPerf/android_kernel_asus_sdm660-LTO.git -b X00TD-P-WIFI-STABLE kernel/asus/sdm660"),
      print("--------------------------------------------------------------------------------------"), 
      os.system("cd && cd " + rdir + " && git clone https://github.com/dhimanparas20/vendor-asus.git vendor/asus "),
      print("--------------------------------------------------------------------------------------"),
      os.system("cd && cd " + rdir + " && git clone https://github.com/dhimanparas20/device_asus_sdm660-common.git device/asus/sdm660-common"),
      print("--------------------------------------------------------------------------------------"),
      os.system("cd && cd " + rdir + " && git clone https://github.com/dhimanparas20/device_asus_X00TD.git -b " + b + " device/asus/X00TD "),
      print("------------------------------------------------------------------------------------------------"))
      
  elif opt == "Y" or opt == "y":
    return(
      print("/////////////////////////////===CLONING NEW TREES===////////////////////////////////////"),
      os.system("cd && cd " + rdir + " && git clone https://github.com/ElectroPerf/android_kernel_asus_sdm660-LTO.git -b X00TD-P-WIFI-STABLE kernel/asus/sdm660"),
      print("--------------------------------------------------------------------------------------"), 
      os.system("cd && cd " + rdir + " && git clone https://github.com/dhimanparas20/nvt.git vendor/asus "),
      print("--------------------------------------------------------------------------------------"),
      os.system("cd && cd " + rdir + " && git clone https://github.com/dhimanparas20/cdt.git device/asus/sdm660-common"),
      print("--------------------------------------------------------------------------------------"),
      os.system("cd && cd " + rdir + " && git clone https://github.com/dhimanparas20/dt.git -b " + b + " device/asus/X00TD "),
      print("------------------------------------------------------------------------------------------------"))
