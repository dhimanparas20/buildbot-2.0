import os
import time
import sync

os.system("clear")
print("-----------------------------------------------------------------------------------------")
print("--------------------WELCOME TO COMPILING SCRIPT BY MST PRODUCTIONS-----------------------")
print("-----------------------------------------------------------------------------------------")
print()
print()

time.sleep(1)

print ("------------------------------------------------")
print ("            Choose your Choice                  ")
print ("------------------------------------------------")
print ("0: Save Github credentials ")
print ("1: sync Rom Repo")
print ("2: sync Device Trees ")
print ("3: Compile rom ")
print ("4: Upload rom to GD ")
print ("5: do 1,2 together")
print ("6: do 1,2,3,4 together ")
print ("press any other key to exit :") 
print("--------------------------------------------------")
print()
print()
print("==================================================")
inp = int(input("Enter your choice :"))
print("==================================================")
print()
print()
time.sleep(1)

#0- saving credentials
if inp == 0 :
  os.system("git config --global credential.helper store")
  print()
  print("-----------------------------------------------")
  print(" work done now exiting.... ")
  time.sleep(3)
  exit()

#1- sync the rom source  
elif inp == 1 :
  print()
  print()
  print ("------------------------------------------------")
  print ("            Choose rom Choice to sync           ")
  print ("------------------------------------------------")
  print ("1: CherishOS")
  print ("2: Cr-Droid ")
  print ("3: DotOS ")
  print ("4: LegionOS ")
  print ("5: Octavi OS")
  print("==================================================")
  choice =  int(input("Enter your choice (number only) : "))
  rdir_name = input("enter the name of new directory : ")
  print("==================================================")
  print()
  print()
  sync.tree(choice,rdir_name)
  print()
  print("----------Work Done , Exiting ---------------")
  time.sleep(3)
  exit()
 
#2- sync the device trees 
elif inp == 2 :
  branch = input("Enter exact name of branch : ")
  rdir_name = input("enter the name of directory : ")
  print("==================================================")  
  print()
  print()
  sync.tree(branch,rdir_name)
  print()
  print("----------Work Done , Exiting ---------------")
  time.sleep(1)
  exit()

#3- compiling the rom 
elif inp == 3 :
  print()
  print()
  print ("------------------------------------------------")
  print ("            Choose rom Choice to compile           ")
  print ("------------------------------------------------")
  print ("1: CherishOS")
  print ("2: Cr-Droid ")
  print ("3: DotOS ")
  print ("4: LegionOS ")
  print ("5: Octavi OS")
  print("==================================================")
  choice =  int(input("Enter your choice (number only) : "))
  rdir_name = input("enter the name of directory : ")
  if choice == 1 :
    os.system("cd && cd buildbot && cp cherish.sh /home/mst/"+ rdir_name )
    os.system("cd && cd " + rdir_name + " && bash cherish.sh ")
  elif choice == 2 :
    os.system("cd && cd buildbot && cp cr.sh /home/mst/"+ rdir_name )
    os.system("cd && cd " + rdir_name + " && rm -rf frameworks/base && rm -rf packages/apps/Settings && rm -rf packages/apps/OctaviLab && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/frameworks_base.git frameworks/base && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/android_packages_apps_Settings.git packages/apps/Settings && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/android_packages_apps_OctaviLab.git packages/apps/OctaviLab ")
    os.system("cd && cd " + rdir_name + " && cd packages/apps/Settings/res/drawable/ && cp ic_device_x00td.png x00td.png ")
    os.system("cd && cd " + rdir_name + " && cd packages/apps/Settings/src/com/android/settings/ && rm -rf AboutPhoneData.java ")
    os.system("cp AboutPhoneData.java /home/mst/"+ rdir +"/packages/apps/Settings/src/com/android/settings")
    print("-----------------------------------Issues Fixed ----------------------------------------------")
    os.system("cd && cd " + rdir_name + " && bash cr.sh ")
  elif choice == 3 :
    os.system("cd && cd buildbot && cp dot.sh /home/mst/"+ rdir_name )
    os.system("cd && cd " + rdir_name + " && bash dot.sh ")
  elif choice == 4 :
    os.system("cd && cd buildbot && cp legion.sh /home/mst/"+ rdir_name )
    os.system("cd && cd " + rdir_name + " && bash legion.sh ")
  elif choice == 5 :
    os.system("cd && cd buildbot && cp octavi.sh /home/mst/"+ rdir_name )
    os.system("cd && cd " + rdir_name + " && bash octavi.sh ")

#4- uploading the rom     
elif inp == 4 : 
  rdir_name = input("enter the name of directory : ")
  os.system("cd && cd "+rdir_name +" && cd o*/t*/p*/X* && ls ")
  print("----------------------------------------------------------------------------------")
  name = input("paste the name of file you want to upload : ")
  print("--------------------------------uploading-----------------------------------------")
  print()
  os.system("cd && cd "+rdir_name +" && cd o*/t*/p*/X*  && rclone sync " + name + " gd: ")
  print("---------------------------------file uploaded------------------------------------")
  print("exitind now ......")
  time.sleep(2)
  exit()  
  
# 1,2 together
elif inp == 5 :
  print()
  print()
  #1
  print ("------------------------------------------------")
  print ("            Choose rom Choice to sync           ")
  print ("------------------------------------------------")
  print ("1: CherishOS")
  print ("2: Cr-Droid ")
  print ("3: DotOS ")
  print ("4: LegionOS ")
  print ("5: Octavi OS")
  print("==================================================")
  choice =  int(input("Enter your choice (number only) : "))
  rdir_name = input("enter the name of new directory : ")
  branch = input("Enter exact name of branch : ")
  print("==================================================")
  print()
  print()
  sync.tree(choice,rdir_name)
  print()
  print("----------Work Done -----------------------------")
  #2
  print("----------------syncing trees --------------------")
  print("==================================================")  
  print()
  print()
  sync.tree(branch,rdir_name)
  print()
  print("----------Work Done , Exiting ---------------")
  time.sleep(3)
  exit() 
  
# 1,2,3,4 together
elif inp == 6: 
  print()
  print()
 
  #1
  print ("------------------------------------------------")
  print ("            Choose rom Choice to sync           ")
  print ("------------------------------------------------")
  print ("1: CherishOS")
  print ("2: Cr-Droid ")
  print ("3: DotOS ")
  print ("4: LegionOS ")
  print ("5: Octavi OS")
  print("==================================================")
  choice =  int(input("Enter your choice (number only) : "))
  rdir_name = input("enter the name of new directory : ")
  branch = input("Enter exact name of branch : ")
  print("==================================================")
  print()
  print()
  sync.tree(choice,rdir_name)
  print()
  print("----------Work Done -----------------------------")
 
  #2
  print("----------------syncing trees --------------------")
  print("==================================================")  
  print()
  print()
  sync.tree(branch,rdir_name)
  print()
  print("------------------Work Done ---------------------")
  
  #3
  print("-----------------Starting Build------------------")
  choice =  int(input("Enter your choice (number only) : "))
  rdir_name = input("enter the name of directory : ")
  if choice == 1 :
    os.system("cd && cd buildbot && cp cherish.sh /home/mst/"+ rdir_name )
    os.system("cd && cd " + rdir_name + " && bash cherish.sh ")
  elif choice == 2 :
    os.system("cd && cd buildbot && cp cr.sh /home/mst/"+ rdir_name )
    os.system("cd && cd " + rdir_name + " && rm -rf frameworks/base && rm -rf packages/apps/Settings && rm -rf packages/apps/OctaviLab && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/frameworks_base.git frameworks/base && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/android_packages_apps_Settings.git packages/apps/Settings && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/android_packages_apps_OctaviLab.git packages/apps/OctaviLab ")
    os.system("cd && cd " + rdir_name + " && cd packages/apps/Settings/res/drawable/ && cp ic_device_x00td.png x00td.png ")
    os.system("cd && cd " + rdir_name + " && cd packages/apps/Settings/src/com/android/settings/ && rm -rf AboutPhoneData.java ")
    os.system("cp AboutPhoneData.java /home/mst/"+ rdir +"/packages/apps/Settings/src/com/android/settings")
    print("-----------------------------------Issues Fixed ----------------------------------------------")
    os.system("cd && cd " + rdir_name + " && bash cr.sh ")
  elif choice == 3 :
    os.system("cd && cd buildbot && cp dot.sh /home/mst/"+ rdir_name )
    os.system("cd && cd " + rdir_name + " && bash dot.sh ")
  elif choice == 4 :
    os.system("cd && cd buildbot && cp legion.sh /home/mst/"+ rdir_name )
    os.system("cd && cd " + rdir_name + " && bash legion.sh ")
  elif choice == 5 :
    os.system("cd && cd buildbot && cp octavi.sh /home/mst/"+ rdir_name )
    os.system("cd && cd " + rdir_name + " && bash octavi.sh ")
  print("------------------Work Done ---------------------")
  print("----------------Starting Upload------------------")  
  
  #4
  rdir_name = input("enter the name of directory : ")
  os.system("cd && cd "+rdir_name +" && cd o*/t*/p*/X* && ls ")
  print("--------------------------------uploading-----------------------------------------")
  print()
  os.system("cd && cd "+rdir_name +" && cd o*/t*/p*/X*  && rclone sync " + name + " gd: ")
  print("---------------------------------file uploaded------------------------------------")
  print("exitind now ......")
  time.sleep(2)
  exit()  
  
else :
  print("ERROR: Invalid input ")
  print("Exiting......")
  time.sleep(4)
  exit()
 
