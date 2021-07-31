#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
from datetime import time
from datetime import timedelta


# Complete the time_delta function below.
def time_delta(t1, t2):
    
    d1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    d2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    secs1=d1.timestamp()  #timezone in d1 in seconds
    secs2=d2.timestamp()  #timezone in d1 in seconds
    sec_diff=int(secs1-secs2) #diff between timezones in seconds
    sec_diff=abs(sec_diff)
    sec_diff=str(sec_diff)
    print("sec_diff ",sec_diff)
    return sec_diff
    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

        #fptr.close()

