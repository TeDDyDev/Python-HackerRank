#!/bin/python3

import math
import os
import random
import re
import sys



n=int(input())
if n%2==0 and 5>=n>=2:
    print("Not Weird")
elif n%2==0 and n>20:
    print("Not Weird")
elif n%2==0 and 20>=n>=6:
    print("Weird")  
else:  
    print("Weird") 