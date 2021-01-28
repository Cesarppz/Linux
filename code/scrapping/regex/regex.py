#!/usr/bin/python3
import re

pattern = re.compile(r'^[\d]{4}.+,(\w+),(\w+),(\d)+,(\d+),.*$')

with open('practr.csv','r') as f :
    
    for line in f:
        res = re.match(pattern,line)
        
        if res :
            total = int(res.group(3)) + int(res.group(4))
            if total >= 8:
                print(f'{res.group(1)} => {res.group(3)},\t{res.group(2)} => {res.group(4)}')

# 2018-06-04,Serbia,Chile,0,1,Friendly,Graz,Austria,TRUE
