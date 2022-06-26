# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 07:55:13 2022

@author: Patricio Haro
"""



import os
print("Dimención de lista entre 5 y 30")
n1=int(input("digite dimencion 1: "))
n2=int(input("digite dimencion 2: "))
if n1>=5 and n2<=30:
    print("")
else:
    print("dimencion fuera de rango")
op=int(input("que operacion matematica desea hacer:"))
suma=n1=[1,2,3,4,5,6,7,8,9,10]
n2=[1,2,3,4,5,6,7,8,9,10]
n3=[0]*10
for item in range(10):
    n3[item]=n1[item]+n2[item]
for item in range(10):
    print(n3[item],end=" ")
print("\n")
print(n3)
resta=n1=[1,2,3,4,5,6,7,8,9,10]
n2=[1,2,3,4,5,6,7,8,9,10]
n3=[0]*10
for item in range(10):
    n3[item]=n1[item]-n2[item]
for item in range(10):
    print(n3[item],end=" ")
print("\n")
print(n3)
producto=n1=[1,2,3,4,5,6,7,8,9,10]
n2=[1,2,3,4,5,6,7,8,9,10]
n3=[0]*10
for item in range(10):
    n3[item]=n1[item]*n2[item]
for item in range(10):
    print(n3[item],end=" ")
print("\n")
print(n3)
if n2!=0:
    cociente=n1=[1,2,3,4,5,6,7,8,9,10]
    n2=[1,2,3,4,5,6,7,8,9,10]
    n3=[0]*10
    for item in range(10):
        n3[item]=n1[item]+n2[item]
    for item in range(10):
        print(n3[item],end=" ")
    print("\n")
    print(n3)
else:
    cociente=0


