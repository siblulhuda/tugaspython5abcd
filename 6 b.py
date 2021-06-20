# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 05:20:21 2021

@author: Dell
"""

#Pengulangan Program 
Jwb = "y"
while Jwb =="y" or Jwb =="Y":
    print("-----------------")
    print(" Transaksi Pembelian Printer diskon 15 % jika nominal > 1,5jt")
    print("-----------------")
    
    #Nilai awal variable jmlBeli = harga 1 printer
    
    HargaPrint = 660000
    
    #HargaPrint = input("Masukkan harga printer Epson T20 =  ")
    
    #Input Jumlah Beli 
    jmlbeli = input("Masukkan Jumlah Printer Epson T20 Yang Dibeli=  ")
    
    x = int(HargaPrint) * int(jmlbeli) * (15/100)
    
    #Proses Hitung Total
    #Total = int(HargaPrint) * int(jmlbeli)
    
    if int((HargaPrint) * int(jmlbeli)) > 1500000:
    #    status = int(((HargaPrint) * int(jmlbeli)) - (15 / 100)) 
        status = int((HargaPrint) * int(jmlbeli)) - x 
    else :
        status = int((HargaPrint) * int(jmlbeli))
    #    status = int(((HargaPrint) * int(jmlbeli))- (100/100))
    print ("Total Transaksi Pembelian Printer Epson T20 = Rp " + str (status))
    
    #if int(Total) < 1500000:
    #    status = ("Total Transaksi Pembelian Printer Epson T20 = Rp " + str (Total))
    #Tampil
    #print("Total Transaksi Pembelian Printer Epson T20 = Rp " + str (Total))
    #else:
    #    status = ("Totallll Transaksi Pembelian Printer Epson T20 = Rp " + str (Total))
    #print("Total Transaksi Pembelian Printer Epson T20 = Rp " + str (Total))
    
    #print(status)
    #inputan untuk break       
    Jwb = input(" >>> Apakah Anda ingin memulai program ulang ? y/t :  ")
    if Jwb == "t" or Jwb == "T":
        break
