#!/usr/bin/python3
# coder: axcisstheproject
# *-* coding: utf-8 *-*
# ronkw0rk

# items  > temp files lost 

#from random import random
import  sys 
import turtle 
from turtle import *
import time 



banner = [
    "#########################################################",
    "################ $$$$$$$$$$$$$$$$$$$$$$$    #############",
    "###########  $$$$$$$  #############   $$$$$$$$  #########",
    "###########  $$$$$$$  ############     $$$$$$  ##########",
    "################ $$$$$$### $$$$$$$$$$$$$$       #########",
    "####################### $$$$ #########  ###  ###  ## # ##",
    "####################### $$$$ ######## ###### ## # #### ##",
    "########################## ########### ##### # ##########",
         "VECTOR GRAPHICS ON SECUENCE ONLY NET DISTURBE "


]




def pointers():
    if str(sys.argv[1]) == '-p' or str(sys.argv[1]) == '--pointer':
        
        makker = sys.argv[2]
        #if end :
        #    pass
    elif str(sys.argv[1]) == '-h' or str(sys.argv[1]) == '--help':
        print('sample is config  vector operation code is now try')
        print('options ' + 'collective: --help  | -h ')
        #print()



def functions(kw , kx, ky, kz):
    line = 45 # operation force all segment 
    #builder=tt.Turtle()
    #showturtle()
    
    # operation lambda all functions 
    if kx > 10  and  ky > 10 : 
        
        persistian = lambda x : x * 10 - line 
        
    elif kw < 10 and  kz < 10:
        strooper = lambda z : z * 10 - line 
    else:
        print('error create pointer check results ')
        sys.exit(1)

if __name__ == "__main__":
    #print(banner[0:], end="\n") 
    for osffet in  range(0,9):
        time.sleep(0.2)
        print(banner[osffet])
        #print(banner[1])
    #functions()