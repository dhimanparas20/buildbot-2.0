#module to upload the rom to gdrive or sourceforge
#Note: your rclone must be configured..

import os
import time

def gd (rdir_name,name):
  return(
    print("--------------------------------uploading-----------------------------------------"),
    os.system("cd && cd "+rdir_name+" && cd o*/t*/p*/X*  && rclone sync "+name+" gd: "),
    print("---------------------------------file uploaded------------------------------------"),
    print("exitind now ......"),
    time.sleep(2),
    exit())
 
 
def sf (rdir_name,name,proj):
  return(
    print("--------------------------------uploading-----------------------------------------"),
    print(),
    os.system("cd && cd "+rdir_name+" && cd o*/t*/p*/X* && scp "+name+" mst-2069@frs.sourceforge.net:/home/frs/project/"+proj ),
    print("---------------------------------file uploaded------------------------------------"),
    print("exitind now ......"),
    time.sleep(2),
    exit())
      
    