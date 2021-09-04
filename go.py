import os
import time
import sync
import up 
import code
import vars

print(code.VIOLET+"#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print(code.RED+"#------------------"+code.END+code.HIGHLIGHT+code.RED+"=================================================="+code.END+code.RED+"---------------------#")
print("#------------------"+code.END+code.HIGHLIGHT+code.RED+"| WELCOME TO COMPILING SCRIPT BY MST PRODUCTIONS |"+code.END+code.RED+"---------------------#")
print("#------------------"+code.END+code.HIGHLIGHT+code.RED+"=================================================="+code.END+code.RED+"---------------------#"+code.END)
print(code.VIOLET+"#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#----------------------------------------------------------------------"+code.END+code.HIGHLIGHT+code.RED+"BY: Paras Dhiman --#"+code.END)
print()

time.sleep(1)

print (code.RED+"------------------------------------------------")
print (code.VIOLET+"            Choose your Choice                  ")
print (code.RED+"------------------------------------------------")
print (code.GREEN+"0: Save Github credentials ")
print ("1: sync Rom Repo")
print ("2: sync Device Trees ")
print ("3: Upload rom to GD or SF ")
print ("4: Setup Build Environment")
print ("5: Generate SSH Key")
print ("99: exit the code "+code.END)
print(code.RED+"================================================")
inp = int(input(code.CYAN+"Enter your choice :"))
print(code.RED+"================================================")
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
  choice =  int(input(code.GREEN+"Enter your choice (number only) : "+code.END))
  rdir_name = input(code.GREEN+"enter the name of new directory : "+code.END)
  print(code.CYAN+"=================================================="+code.END)
  print()
  start_time = time.time()
  sync.repo(choice,rdir_name)
  print(code.RED+"-------------------------- %s seconds -----------------------------" % (time.time() - start_time))
  print()
  time.sleep(1)
  code.loop()
 
 
#2- sync the device trees 
elif inp == 2 :
  print(code.VIOLET+"==================================================") 
  rdir_name = input(code.YELLOW+"enter the name of working directory: ")
  branch = input(code.YELLOW+"Enter exact name of github branch: ")
  print(code.VIOLET+"==================================================")  
  print()
  start_time = time.time()
  sync.tree(branch,rdir_name)
  print(code.RED+"---------------------- %s seconds -------------------------" % (time.time() - start_time))
  print()
  time.sleep(1)
  code.loop()
 
#3- uploading the rom
elif inp == 3 :
  print (code.VIOLET+"------------------------------------------------")
  print (code.YELLOW+"            Available Options          ")
  print (code.VIOLET+"------------------------------------------------")
  print (code.YELLOW+"1: Gdrive")
  print ("2: Source Forge ")
  print(code.VIOLET+"==================================================")
  cho = int(input(code.YELLOW+"enter where you want to upload : "))
  print(code.VIOLET+"==================================================")
  print()
  os.system("clear")
  if cho == 1 :
    print(code.VIOLET+"-----------------------------------------------------------------------------")
    rdir_name = input(code.YELLOW+"enter the name of working directory : ")
    print(code.VIOLET+"-----------------------------------------------------------------------------")
    print()
    os.system("cd && cd "+rdir_name+" && cd " +vars.OUT+ "&& ls")
    print()
    print(code.VIOLET+"-----------------------------------------------------------------------------")
    name = input(code.YELLOW+"Enter the name of file: ")
    os.system("clear")
    start_time = time.time()
    up.gd(rdir_name,name)
    print(code.RED+"---------------------------- %s seconds -------------------------------" % (time.time() - start_time))
    code.loop()

  elif cho == 2 :
    print(code.VIOLET+"-----------------------------------------------------------------------------")
    rdir_name = input(code.YELLOW+"enter the name of working directory : ")
    print(code.VIOLET+"-----------------------------------------------------------------------------")
    print()
    os.system("cd && cd "+rdir_name+" && cd " +vars.OUT+ "&& ls")
    print()
    print(code.VIOLET+"-----------------------------------------------------------------------------")
    name = input(code.YELLOW+"Enter the name of file: ")
    proj = input(code.YELLOW+"Enter the name of project (without first slash) and location: ")
    print(code.VIOLET+"-----------------------------------------------------------------------------")
    os.system("clear")
    start_time = time.time()
    up.sf(rdir_name,name,proj)
    print(code.RED+"---------------- %s seconds -------------------" % (time.time() - start_time))
    code.loop()
    
# Build Environment 
elif inp == 4 :
  print(code.VIOLET+"-----------------------------------------------------------------------------")
  print(code.VIOLET+" This script will set your build environment for newly made server or terminal ")
  print(code.VIOLET+" All the dependencies and files will be downloaded automatically ")
  print(code.GREEN+"==================================================")
  inp = input(code.YELLOW+"Press Y to proceed or N to return: ")
  print(code.GREEN+"==================================================")
  if inp == 'y' or inp == "y" :
    start_time = time.time()
    os.system("./env.sh")
    print(code.RED+"---------------- %s seconds -------------------" % (time.time() - start_time))
  elif inp == 'n' or inp == 'N' :
    code.loop()  
    
# Generating SSH key
elif inp == 5 :
  os.system("python3 addkey.py")   
        
# Exit
elif inp == 99 :
  code.exit()

# Wrong_Input
else :
  print(code.RED+"---------------WRONG INPUT------------------"+code.END)
  code.loop() 
