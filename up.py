#module to upload the rom to gdrive or sourceforge
#Note: your rclone must be configured..

import os
import time
import vars
import code

def gd (rdir_name,name):
  return(
    print(code.RED+"--------------------------------uploading to Gdrive-----------------------------------------"+code.END),
    os.system("cd && cd "+rdir_name+" && cd " +vars.OUT+ " && rclone sync "+name+ " " +vars.RC),
    print(code.GREEN+"││"),
    print("││││"),
    print("││││││"),
    print("││││││││"),
    print("││││││││││"),
    print("││││││││││││"),
    print("││││││││││││││"),
    print("││││││││││││││││"),
    print("││││││││││││││││││"),
    print("││││││││││││││││││││"),
    print(code.RED+"---------------------------------file uploaded------------------------------------"),
    print(code.CYAN+"exiting now ......"),
    time.sleep(1))
     
 
def sf (rdir_name,name,proj):
  return(
    print(code.RED+"--------------------------------uploading to SF-----------------------------------------"),
    print(),
    os.system("cd && cd "+rdir_name+" && cd "+vars.OUT+" &&ls &&  scp "+name+" "+vars.SF+proj ),
    print(code.GREEN+"││"),
    print("││││"),
    print("││││││"),
    print("││││││││"),
    print("││││││││││"),
    print("││││││││││││"),
    print("││││││││││││││"),
    print("││││││││││││││││"),
    print("││││││││││││││││││"),
    print("││││││││││││││││││││"),
    print(code.RED+"---------------------------------file uploaded------------------------------------"),
    print(code.CYAN+"exiting now ......"),
    time.sleep(1))
