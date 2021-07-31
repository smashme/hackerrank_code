'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


#!/bin/python3

import math
import os
import random
import re
import sys
from array import *


if __name__ == '__main__':
    
    s = input()
    alpha=sorted(s)
    com=0
    alpha.sort(key = lambda x: x.lower())
    array1=array
    array1=[0]*26

    
    ##print("alpha", alpha)
    for i in alpha:
        if (i=='a' or i=='A'):
            array1[0]+=1
        if (i=='b' or i=='B'):
            array1[1]+=1
        if (i=='c' or i=='C'):
            array1[2]+=1
        if (i=='d' or i=='D'):
            array1[3]+=1
        if (i=='e' or i=='E'):
            array1[4]+=1
        if (i=='f' or i=='F'):
            array1[5]+=1
        if (i=='g' or i=='G'):
            array1[6]+=1
        if (i=='h' or i=='H'):
            array1[7]+=1
        if (i=='i' or i=='I'):
            array1[8]+=1
        if (i=='j' or i=='J'):
            array1[9]+=1
        if (i=='k' or i=='K'):
            array1[10]+=1
        if (i=='l' or i=='L'):
            array1[11]+=1
        if (i=='m' or i=='M'):
            array1[12]+=1
        if (i=='n' or i=='N'):
            array1[13]+=1
        if (i=='o' or i=='O'):
            array1[14]+=1
        if (i=='p' or i=='P'):
            array1[15]+=1
        if (i=='q' or i=='Q'):
            array1[16]+=1
        if (i=='r' or i=='R'):
            array1[17]+=1
        if (i=='s' or i=='S'):
            array1[18]+=1
        if (i=='t' or i=='T'):
            array1[19]+=1
        if (i=='u' or i=='U'):
            array1[20]+=1
        if (i=='v' or i=='V'):
            array1[21]+=1
        if (i=='w' or i=='W'):
            array1[22]+=1
        if (i=='x' or i=='X'):
            array1[23]+=1
        if (i=='y' or i=='Y'):
            array1[24]+=1
        if (i=='z' or i=='Z'):
            array1[25]+=1
   
    for u in range (0,25):
        com+=1
        a=(max(array1))
       ## print("a= ",a)
        y=(array1.index(a))
        if (a==0 or a==-1):
           ## print("done")
            break
        if (com<4):
            print(chr(y+97), a)
        array1[y]=-1
        
    
   ### print("i= ",i)
    
    


