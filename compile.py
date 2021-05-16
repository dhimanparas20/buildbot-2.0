import time
import os
import sync
import octavi

def run(choice,rdir_name,inp):
  print("==================================================")
  if choice == 1 :
    return(
      os.system("cd && cd buildbot && cp cherish.sh /home/mst/"+ rdir_name ),
      os.system("cd && cd " + rdir_name + " ls && exit "))
  elif choice == 2 :
    return(
      os.system("cd && cd buildbot && cp cr.sh /home/mst/"+ rdir_name ),
      os.system("cd && cd " + rdir_name + " ls && exit "))
  elif choice == 3 :
    return(
      os.system("cd && cd buildbot && cp dot.sh /home/mst/"+ rdir_name ),
      os.system("cd && cd " + rdir_name + " ls && exit "))
  elif choice == 4 :
    if inp == "y" or inp == "Y" :
      return(
        octavi.fix(rdir_name),
        os.system("cd && cd buildbot && cp octavi.sh /home/mst/"+ rdir_name ),
        os.system("cd && cd " + rdir_name + " ls && exit "))
    elif inp == "n"  or inp == "N" :
      return(
        os.system("cd && cd buildbot && cp octavi.sh /home/mst/"+ rdir_name ),
        os.system("cd && cd " + rdir_name + " ls && exit "))
    else :
      return(
        time.sleep(1),
        print("invalid input"),
        time.sleep(1),
        print("exiting"),
        time.sleep(2),
        exit())
  else:
    return(
      time.sleep(1),
      print("invalid input"),
      time.sleep(1),
      print("exiting"),
      time.sleep(2),
      exit())
    
