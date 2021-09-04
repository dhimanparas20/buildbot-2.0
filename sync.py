#Module to Sync trees and rom source
import os
import time 
import vars
import code 

#display input for rom sync
#displays the choices 

def disp():
  return(
    print(),
    print (code.GREEN+"------------------------------------------------"),
    print (code.CYAN+"            Choose rom Choice to sync           "),
    print (code.GREEN+"------------------------------------------------"),
    print (code.BLUE+"1: ", vars.ROM_NAME1),
    print ("2: ", vars.ROM_NAME2),
    print ("3: ", vars.ROM_NAME3),
    print ("4: ", vars.ROM_NAME4 , code.END),
    print (code.GREEN+"=================================================="+code.END))

#syncing rom repo
def repo (inp,rdir):  
  if inp == 1:
    #rom1
    return(
      os.system("cd && mkdir "+ rdir ),
      os.system("cd && cd " +rdir+ " &&" +vars.ROM_LINK1),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print(code.GREEN+"Repo Sync Complete "+code.END))
    
  
  elif inp == 2 :
    #rom2 
    return(
      os.system("cd && mkdir "+ rdir ),
      os.system("cd && cd " +rdir+ " &&" +vars.ROM_LINK2),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print(code.GREEN+"Repo Sync Complete "+code.END))
    
 
  elif inp == 3 :
    #rom3
    return(
      os.system("cd && mkdir "+ rdir ),
      os.system("cd && cd " +rdir+ " &&" +vars.ROM_LINK3),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print(code.GREEN+"Repo Sync Complete "+code.END))
      
  
  elif inp == 4 :
    #rom4
    return(
      os.system("cd && mkdir "+ rdir ),
      os.system("cd && cd " +rdir+ " &&" +vars.ROM_LINK4),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print(code.GREEN+"Repo Sync Complete "+code.END))

#syncing device trees
def tree (b,rdir):
  return(
    print(code.CYAN+"/////////////////////////////===CLONING TREES===////////////////////////////////////"+code.END),
    os.system("cd && cd " + rdir + " && git clone " +vars.KT+ " " +vars.P_KT+code.END),
    print(code.RED+"--------------------------------------------------------------------------------------"), 
    os.system("cd && cd " + rdir + " && git clone " +vars.VT+ " " +vars.P_VT),
    print(code.RED+"--------------------------------------------------------------------------------------"),
    os.system("cd && cd " + rdir + " && git clone " +vars.CDT+ " " +vars.P_CDT),
    print(code.RED+"--------------------------------------------------------------------------------------"),
    os.system("cd && cd " + rdir + " && git clone " +vars.DT+ " -b " +b+ " " +vars.P_DT),
    print(code.RED+"------------------------------------------------------------------------------------------------"))
