# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 05:05:27 2021

@author: Dell
"""

print("CEK GOLONGAN USIA")
print("-----------------")
n=input("Masukkan Umur =  ")
u=int(n)
if u>60:
    status ="Lansia"
elif u>=35 and u<=59:
    status ="Dewasa"
elif u>=18 and u<=34:
    status ="Pemuda"
elif u>=15 and u<=17:
    status ="Remaja"
else:
    status="Anak"
print(status)