#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    n=s.split(':')
    h1=int(s[0]+s[1])
    mm=int(s[3]+s[4])
    ss=int(s[6]+s[7])
    if s[8]=='P':
        if h1>=1 and h1<12:
            h1=h1+12
    #elif h1==2 and s[8]=='P':
     #   h1=14
    #elif h1==3 and s[8]=='P':
     #   h1=15
    #elif h1==4 and s[8]=='P':
     #   h1=16
    #elif h1==5 and s[8]=='P':
     #   h1=17
    #elif h1==6 and s[8]=='P':
     #   h1=18
    #elif h1==7 and s[8]=='P':
     #   h1=19
    #elif h1==8 and s[8]=='P':
     #   h1=20
    #elif h1==9 and s[8]=='P':
     #   h1=21
    #elif h1==10 and s[8]=='P':
     #   h1=22
    #elif h1==11 and s[8]=='P':
     #   h1=23
    if h1>=12 and s[8]=='A':
        h1=0
    if h1<=9:
        h1='0'+str(h1)
    s1=str(h1)+":"+s[3]+s[4]+":"+s[6]+s[7]
    print ("s1",s1)
    return s1
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

