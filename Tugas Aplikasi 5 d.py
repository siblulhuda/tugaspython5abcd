# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 06:45:52 2021

@author: Dell
"""

print("Penilaian Mahasiswa")
print("-------------------")
n=input("Masukkan Nilai =  ")
x=int(n)
if x>=91 and x<100:
    status="A"
elif x>=81 and x<91:
    status="B"
elif x>71 and x<81:
    status="C"
elif x<71:
    status="D"
else:
    status="masukkan Angka 0 sampai 99"
print(status)
