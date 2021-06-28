# python function to exit or loop the whole code

import os
import time

def loop () :
  return(
    os.system("clear"),
    print(),
    print(),
    print("------------------Returning to main menue------------------------"),
    os.system("./run.sh"))
    
def exit () :
  return(  
    os.system("clear"),
    print(),
    print(),
    print("---------------------Exiting the code------------------------"),   
    os.system("cd && ls"))

def ask (opt) :
  if opt == 1:
    return(
      os.system("clear"),
      print(),
      print(),      
      print("------------------Returning to main menue------------------------"),
      os.system("./run.sh"))
      
  elif opt == 0:
    return(
      os.system("clear"),
      print(),
      print(),
      print("---------------------Exiting the code------------------------"),   
      os.system("cd && ls"))
      
def home (rdir) :
  return(
    os.system("cd && cd " + rdir + " && ls "))   
      
      