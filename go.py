import os
import time
import sync
import up 
import compile
import octavi


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
print ("3: Compile rom ")
print ("4: Upload rom to GD or SF ")
print ("press any other key to exit :") 
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
  print("-----------------------------------------------")
  print(" work done now exiting.... ")
  time.sleep(3)
  exit()

#1- sync the rom source  
elif inp == 1 :
  sync.disp()  
  choice =  int(input("Enter your choice (number only) : "))
  rdir_name = input("enter the name of new directory : ")
  print("==================================================")
  print()
  sync.repo(choice,rdir_name)
  print()
  print("----------Work Done , Exiting ---------------")
  time.sleep(2)
  os.system("clear")
  exit()
 
#2- sync the device trees 
elif inp == 2 :
  print("==================================================") 
  opt = input("Do you want to sync new trees?(Y or N): ")
  branch = input("Enter exact name of github branch : ")
  rdir_name = input("enter the name of directory : ")
  print("==================================================")  
  print()
  sync.tree(opt,branch,rdir_name)
  print()
  print("----------Work Done , Exiting ---------------")
  time.sleep(2)
  os.system("clear")
  exit()

#3- compiling the rom 
elif inp == 3 :
  sync.opt()  
  choice =  int(input("Enter your choice (number only) : "))
  rdir_name = input("enter the name of directory : ")
  if choice == 4 :
    inp = input("Do you want to sync octavi private source? type (y/n): " )
    print("==================================================")
    print()
    compile.run(choice,rdir_name,inp)
    else:  
    print("==================================================")
    print()
    compile.run(choice,rdir_name)
          
#4- uploading the rom     
elif inp == 4 :
  print ("------------------------------------------------")
  print ("            Choose rom Choice to upload          ")
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
    os.system("cd && cd "+rdir_name+" && cd o*/t*/p*/X* && ls ")
    print()
    print("-----------------------------------------------------------------------------")
    name = input("Enter the name of file: ")
    os.system("clear")
    up.gd(rdir_name,name)
    
  elif cho == 2 :
    print("-----------------------------------------------------------------------------")
    rdir_name = input("enter the name of working directory : ")
    print("-----------------------------------------------------------------------------")
    print()
    os.system("cd && cd "+rdir_name+" && cd o*/t*/p*/X* && ls ")
    print()
    print("-----------------------------------------------------------------------------")
    name = input("Enter the name of file: ")
    proj = input("Enter the name of project (without first slash) and location: ")
    print("-----------------------------------------------------------------------------")
    os.system("clear")
    up.sf(rdir_name,name,proj)
