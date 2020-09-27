# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:28:04 2020

@author: Lucas
"""

import pandas as pd
import numpy as np
import math
from bitstring import BitStream, BitArray

def longRunTest(binario):
    zero = ''
    one = ''
    for i in range(34):
        zero = zero + '0'
        one = one + '1'
        
    if zero in binario or one in binario:
        return False
    else:
        return True
        
def runTest(binario):

    contador1=0
    contador0=0
    zeros=[0,0,0,0,0,0,0]
    ones=[0,0,0,0,0,0,0]

    for char in binario:
        if char == '1':
            if contador0!=0:
                if contador0>6:
                    zeros[6]+=1
                else:
                    zeros[contador0]+=1
                contador0=0
            contador1 += 1
        else:
            if contador1!=0:
                if contador1>6:
                    ones[6]+=1
                else:
                    ones[contador1]+=1
                contador1=0
            contador0+=1
    if zeros[1] >= 2267 and zeros[1] <=2733 and ones[1] >= 2267 and ones[1] <=2733:
        if zeros[2] >= 1079 and zeros[2] <=1421 and ones[2] >= 1079 and ones[2] <=1421:
            if zeros[3] >= 502 and zeros[3] <=748 and ones[3] >= 502 and ones[3] <=748:
                if zeros[4] >= 223 and zeros[4] <=402 and ones[4] >= 223 and ones[4] <=402:
                    if zeros[5] >= 90 and zeros[5] <=223 and ones[5] >= 90 and ones[5] <=223:
                        if zeros[6] >= 90 and zeros[6] <=223 and ones[6] >= 90 and ones[6] <=223:
                            return True
    return False

def soma(count):
    
    total = 0
    for i in range(len(count)):
        total = total + count[i]**2
    return total    

def poker(row):
    
    global dic
    count = {}
    for i in range(16):
        count[i] = 0    
    
    for i in row:
        count[dic.index(i)] = count[dic.index(i)] + 1
    
    total = soma(count)
    
    value = ((16/5000)*total)-5000
    
    return value


file = open('C:\\Users\\Lucas\\Downloads\\ChavesdeCriptografia.txt', 'r')
vet = file.read().replace("'",'').replace('\\','').split("\n")

binario = []

for i in range(len(vet)):
    if vet[i] != '':    
        binario.append(BitArray(hex=vet[i]).bin)

#teste 1
test1 = []
zero = []
count = 0    
for row in binario:
    for numb in row:
        if numb == '0':
            count = count +1
    if count > 9654 and count < 103446:
        test1.append('True')
    else:
        test1.append('False')
    count = 0
#teste2
test2 = []
pieces = 4
rows = []
for row in binario:
    rows.append([row[i:i+pieces] for i in range(0, len(row), pieces)])
    
dic = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111',]

pokerR = []

for i in range(len(rows)):
    pokerR.append(poker(rows[i]))
    
for i in pokerR:
    if i > 1.03 and i < 57.4:
        test2.append('True')
    else:
        test2.append('False')
        
#test3
test3 = []

for i in binario:
    test3.append(runTest(i))
#test4
test4 = []     
for i in binario:
    test4.append(longRunTest(i))

df = pd.DataFrame()
df['monobitTest'] = test1
df['pokerTest'] = test2
df['runsTest'] = test3
df['longRunTest'] = test4
  
    
    
            
            
        






        
