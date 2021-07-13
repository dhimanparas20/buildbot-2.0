#module to upload the rom to gdrive or sourceforge
#Note: your rclone must be configured..

import os
import time
import vars

def gd (rdir_name,name):
  return(
    print("--------------------------------uploading to Gdrive-----------------------------------------"),
    os.system("cd && cd "+rdir_name+" && cd " +vars.OUT+ " && rclone sync "+name+ " " +vars.RC),
    print("││"),
    print("││││"),
    print("││││││"),
    print("││││││││"),
    print("││││││││││"),
    print("││││││││││││"),
    print("││││││││││││││"),
    print("││││││││││││││││"),
    print("││││││││││││││││││"),
    print("││││││││││││││││││││"),
    print("---------------------------------file uploaded------------------------------------"),
    print("exiting now ......"),
    time.sleep(1))
     
 
def sf (rdir_name,name,proj):
  return(
    print("--------------------------------uploading to SF-----------------------------------------"),
    print(),
    os.system("cd && cd "+rdir_name+" && cd "+vars.OUT+" &&ls &&  scp "+name+" "+vars.SF+proj ),
    print("││"),
    print("││││"),
    print("││││││"),
    print("││││││││"),
    print("││││││││││"),
    print("││││││││││││"),
    print("││││││││││││││"),
    print("││││││││││││││││"),
    print("││││││││││││││││││"),
    print("││││││││││││││││││││"),
    print("---------------------------------file uploaded------------------------------------"),
    print("exiting now ......"),
    time.sleep(1))
