# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 05:11:13 2021

@author: Dell
"""

print("Menampilkan Nilai Huruf")
print("-----------------------")
n=input("masukkan Nilai =  ")
t=int(n)
if t>100:
    status="Masukkan Angka Antara 0 Sampai 100"
if t>=80 and t<100:
    status="BAIK SEKALI"
elif t>=65 and t<=79:
    status="BAIK"
elif t>=55 and t<=64:
    status="CUKUP"
elif t>=40 and t<=54:
    status="KURANG"
elif t<40 and t>=0:
    status="KURANG SEKALI"
else:
    status="Masukkan Angka Antara 0 sampai 100"
print(status)    