import os
import time
import sync
import up 
import code
import vars

print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#------------------==================================================----------------------#")
print("#------------------| WELCOME TO COMPILING SCRIPT BY MST PRODUCTIONS |---------------------#")
print("#------------------==================================================---------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#----------------------------------------------------------------------BY: Paras Dhiman --#")
print()

time.sleep(1)

print ("------------------------------------------------")
print ("            Choose your Choice                  ")
print ("------------------------------------------------")
print ("0: Save Github credentials ")
print ("1: sync Rom Repo")
print ("2: sync Device Trees ")
print ("3: Upload rom to GD or SF ")
print ("4: Setup Build Environment")
print ("99: exit the code ")
print("==================================================")
inp = int(input("Enter your choice :"))
print("==================================================")
print()
os.system("clear")
time.sleep(1)

#0- saving credentials
if inp == 0 :
  print("-----------------------------------------------")
  start_time = time.time()
  os.system("git config --global credential.helper store")
  print()
  print("-----------------WORK DONE---------------------")
  print("-------- %s seconds --------" % (time.time() - start_time))
  time.sleep(1)
  code.loop()

#1- sync the rom source  
elif inp == 1 :
  sync.disp()  
  choice =  int(input("Enter your choice (number only) : "))
  rdir_name = input("enter the name of new directory : ")
  print("==================================================")
  print()
  start_time = time.time()
  sync.repo(choice,rdir_name)
  print("-------- %s seconds --------" % (time.time() - start_time))
  print()
  time.sleep(1)
  code.loop()
  
 
#2- sync the device trees 
elif inp == 2 :
  print("==================================================") 
  octa = input("Do you want to sync octavi trees and priavte repo? (Y or N): ")
  if octa == "n" or octa == "N" :
    opt = input("Do you want to sync new trees?(Y or N): ")
    rdir_name = input("enter the name of working directory: ")
    branch = input("Enter exact name of github branch: ")
    print("==================================================")  
    print()
    start_time = time.time()
    sync.tree(opt,branch,rdir_name)
    print("---------------------- %s seconds -------------------------" % (time.time() - start_time))
    print()
    time.sleep(1)
    code.loop()
  elif octa == "y" or octa == "Y" : 
    rdir_name = input("enter the name of working OctaviOS directory: ")
    start_time = time.time()
    octavi.fix(rdir_name)  
    print("---------------------- %s seconds -------------------------" % (time.time() - start_time))
    time.sleep(1)
    code.loop()
  else :
    print("wrong choice ")
    code.loop()
           
#3- uploading the rom     
elif inp == 3 :
  print ("------------------------------------------------")
  print ("            Available Options          ")
  print ("------------------------------------------------")
  print ("1: Gdrive")
  print ("2: Source Forge ")
  print("==================================================")
  cho = int(input("enter where you want to upload : "))
  print("==================================================")
  print()
  os.system("clear")
  if cho == 1 :
    print("-----------------------------------------------------------------------------")
    rdir_name = input("enter the name of working directory : ")
    print("-----------------------------------------------------------------------------")
    print()
    os.system("cd && cd "+rdir_name+" && cd " +vars.OUT+ "&& ls")
    print()
    print("-----------------------------------------------------------------------------")
    name = input("Enter the name of file: ")
    os.system("clear")
    start_time = time.time()
    up.gd(rdir_name,name)
    print("---------------------------- %s seconds -------------------------------" % (time.time() - start_time))
    code.loop()
    
  elif cho == 2 :
    print("-----------------------------------------------------------------------------")
    rdir_name = input("enter the name of working directory : ")
    print("-----------------------------------------------------------------------------")
    print()
    os.system("cd && cd "+rdir_name+" && cd " +vars.OUT+ "&& ls")
    print()
    print("-----------------------------------------------------------------------------")
    name = input("Enter the name of file: ")
    proj = input("Enter the name of project (without first slash) and location: ")
    print("-----------------------------------------------------------------------------")
    os.system("clear")
    start_time = time.time()
    up.sf(rdir_name,name,proj)
    print("---------------- %s seconds -------------------" % (time.time() - start_time))
    code.loop()
    
# Build Environment 
elif inp == 4 :
  print("-----------------------------------------------------------------------------")
  print(" This script will set your build environment for newly made server or terminal ")
  print(" All the dependencies and files will be downloaded automatically ")
  print("==================================================")
  inp = input("Press Y to proceed or N to return: ")
  print("==================================================")
  if inp == 'y' or inp == "y" :
    start_time = time.time()
    os.system("./env.sh")
    print("---------------- %s seconds -------------------" % (time.time() - start_time))
  elif inp == 'n' or inp == 'N' :
    code.loop()            
        
# Exit
elif inp == 99 :
  code.exit()

# Wrong_Input
else :
  print("---------------WRONG INPUT------------------")
  code.loop()  
