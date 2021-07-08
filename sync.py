#Module to Sync trees and rom source
import os
import time 
import vars

#display input for rom sync
#displays the choices 
def disp():
  return(
    print(),
    print ("------------------------------------------------"),
    print ("            Choose rom Choice to sync           "),
    print ("------------------------------------------------"),
    print ("1: ", vars.ROM_NAME1),
    print ("2: ", vars.ROM_NAME2),
    print ("3: ", vars.ROM_NAME3),
    print ("4: ", vars.ROM_NAME4),
    print ("=================================================="))

#syncing rom repo
def repo (inp,rdir):
  
  if inp == 1:
    #rom1
    return(
      os.system("cd && mkdir "+ rdir ),
      os.system("cd && cd " +rdir+ " &&" +vars.ROM_LINK1),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print("Repo Sync Complete "))
    
  
  elif inp == 2 :
    #rom2 
    return(
      os.system("cd && mkdir "+ rdir ),
      os.system("cd && cd " +rdir+ " &&" +vars.ROM_LINK2),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print("Repo Sync Complete "))
    
 
  elif inp == 3 :
    #rom3
    return(
      os.system("cd && mkdir "+ rdir ),
      os.system("cd && cd " +rdir+ " &&" +vars.ROM_LINK3),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print("Repo Sync Complete "))
      
  
  elif inp == 4 :
    #rom4
    return(
      os.system("cd && mkdir "+ rdir ),
      os.system("cd && cd " +rdir+ " &&" +vars.ROM_LINK4),
      print("--------------------------------------------------------------------------------------"),
      time.sleep(3),
      print("Repo Sync Complete ")) 

#syncing device trees
def tree (b,rdir):
  return(
    print("/////////////////////////////===CLONING OLD TREES===////////////////////////////////////"),
    os.system("cd && cd " + rdir + " && git clone " +vars.KT+ " " +vars.P_KT),
    print("--------------------------------------------------------------------------------------"), 
    os.system("cd && cd " + rdir + " && git clone " +vars.VT+ " " +vars.P_VT),
    print("--------------------------------------------------------------------------------------"),
    os.system("cd && cd " + rdir + " && git clone " +vars.CDT+ " " +vars.P_CDT),
    print("--------------------------------------------------------------------------------------"),
    os.system("cd && cd " + rdir + " && git clone " +vars.DT+ " -b " +b+ " " +vars.P_DT),
    print("------------------------------------------------------------------------------------------------"))
