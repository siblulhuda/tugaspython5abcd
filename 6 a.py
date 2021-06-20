# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:21:20 2021

@author: KBM I-2
"""
#PengulanganProgram
Jwb = "y"
while Jwb =="y" or Jwb =="Y":
    print("---------------------")
    print("Transasksi Pembelian Printer Epson T20")
    print("---------------------")
    
    #Nilai awal variable jmlbeli = Harga 1 Printer
    HargaPrint = 600000
    jmlbeli = input("Masukkan Jumlah printer Epson T20 Yang Dibeli = ")

    #Proses Hitung Total 
    Total = int(HargaPrint)*int(jmlbeli)

    #Tampil
    print("Total Transaksi Pembelian Printer Epson T20 =Rp " + str (Total))

    #Inputan untuk break
    Jwb = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if Jwb == "t" or Jwb =="T":
        break