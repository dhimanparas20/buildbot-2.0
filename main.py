import os
import time
import sync

print("-----------------------------------------------------------------------------------------")
print("--------------------WELCOME TO COMPILING SCRIPT BY MST PRODUCTIONS-----------------------")
print("-----------------------------------------------------------------------------------------")
print()
print()

time.sleep(3)

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
input = int(input("Enter your choice :"))
print("==================================================")
print()
print()
time.sleep(3)

#0- saving credentials
if inp == 0 :
  os.system("git config --global credential.helper store")
  printt()
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
  choice =  int(input("Enter your choice (number only) : ")
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
  time.sleep(3)
  exit()

#3- compiling the rom 
elif inp == 3 :
  rdir_name = input("enter the name of directory : ")
  if inp == 1 :
    os.system("cd && cd " + rdir_name )
    os.system("bash cherish.sh ")
  elif inp == 2 :
    os.system("cd && cd " + rdir_name )
    os.system("bash cr.sh ")
  elif inp == 3 :
    os.system("cd && cd " + rdir_name )
    os.system("bash dot.sh ")
  elif inp == 4 :
    os.system("cd && cd " + rdir_name )
    os.system("bash legion.sh ")
  elif inp == 5 :
    os.system("cd && cd " + rdir_name )
    os.system("bash octavi.sh ")

#4- uploading the rom     
elif inp == 4 :
  rdir_name = input("enter the name of directory : ")
  os.system("cd ")
  os.system("cd " + rdir_name )
  os.system("cd o*/t*/p*/X* ")
  os.system("ls")
  name = input("paste the name of file you want to upload : ")
  os.system("rclone sync " + name + " gd: ")
  print("-----------file uploaded-----------------")
  print("exitind now ......")
  time.sleep(3)
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
  choice =  int(input("Enter your choice (number only) : ")
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
  choice =  int(input("Enter your choice (number only) : ")
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
  if inp == 1 :
    os.system("cd && cd " + rdir_name )
    os.system("bash cherish.sh ")
  elif inp == 2 :
    os.system("cd && cd " + rdir_name )
    os.system("bash cr.sh ")
  elif inp == 3 :
    os.system("cd && cd " + rdir_name )
    os.system("bash dot.sh ")
  elif inp == 4 :
    os.system("cd && cd " + rdir_name )
    os.system("bash legion.sh ")
  elif inp == 5 :
    os.system("cd && cd " + rdir_name )
    os.system("bash octavi.sh ")
  print("------------------Work Done ---------------------")
  print("----------------Starting Upload------------------")  
  
  #4
  os.system("cd ")
  os.system("cd " + rdir_name )
  os.system("cd o*/t*/p*/X* ")
  os.system("ls")
  name = input("paste the name of file you want to upload : ")
  os.system("rclone sync " + name + " gd: ")
  print("-----------file uploaded-----------------")
  print("exitind now ......")
  time.sleep(3)
  exit()  
  
else :
  print("ERROR: Invalid input ")
  print("Exiting......")
  time.sleep(4)
  exit()
 
