# -*- coding: utf-8 -*-
import os
import sys
try:
    abcint =  sys.argv[1]

except Exception as q:
    print(q)
version="20230073101"
path = "Packages"
with open(path,'r',encoding="utf-8",newline="\n") as f:
    filea = f.read()

fileb = filea.split("\n")

time = 0
numa = 0 
while time < len(fileb):
    filec = fileb[time].split(":")
    if filec[0] == "Filename":
        numa = numa + 1
        #print(str(numa) + "." + filec[1])
        if str(numa) == abcint:
            print(filec[1])
    
    time = time + 1
    
