import os
import time
import sync
import up 
import octavi
import code
import vars


os.system("clear")
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
  os.system("git config --global credential.helper store")
  print()
  print("-----------------WORK DONE---------------------")
  time.sleep(1)
  code.loop()

#1- sync the rom source  
elif inp == 1 :
  sync.disp()  
  choice =  int(input("Enter your choice (number only) : "))
  rdir_name = input("enter the name of new directory : ")
  print("==================================================")
  print()
  sync.repo(choice,rdir_name)
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
    sync.tree(opt,branch,rdir_name)
    print()
    time.sleep(1)
    code.home(rdir_name)
  elif octa == "y" or octa == "Y" : 
    rdir_name = input("enter the name of working OctaviOS directory: ")
    octavi.fix(rdir_name)  
    time.sleep(1)
    code.home(rdir_name)   
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
    up.gd(rdir_name,name)
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
    up.sf(rdir_name,name,proj)
    code.loop()
    
# Exit
elif inp == 99 :
  code.exit()

# Wrong_Input
else :
  print("---------------WRONG INPUT------------------")
  code.loop()  
