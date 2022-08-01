# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. #For example, alison heck should be capitalised correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.


#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    result=[]
    name=re.split(r'(\s+)',s)

    for i in range(len(name)):
       result.append(str(name[i]).capitalize())
       
    
    return ''.join(str(ele) for ele in result)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
