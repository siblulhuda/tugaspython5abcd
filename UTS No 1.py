# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 08:34:35 2021

@author: Dell
"""

"""
Buat program untuk menghitung biaya total pengiriman barang di Lorena Kota Malang
1. set variabel , kota , jarak , ongkirperkm , totongkir
2. input pilihan kota
3. jika kota sby, jarak = 169, ongkirperkm = 2500 , selain itu 
jika kota Bdg,jarak = 452, ongkirperkm = 4000
4.totongkir = jarak * ongkirperkm
5. tampilkan kota, totongkir
"""

Jwb = "y"
while Jwb =="y" or Jwb =="Y":
    print("==============================================================")
    print(" Transaksi Biaya Ekspedisi ")
    print("==============================================================")
    print(" Kode = A. Surabaya")
    print(" Kode = B. Bandung")
    print("==============================================================")
    
    kota = ['surabaya','bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]
    
    pilihan = input(">> Masukkan Kode Tujuan = ")
    #identifikasi pilihan 
    if pilihan== "a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    else:
        idx = 0
        
    #Cetak tampilan layar
    print(">>> Pilihan Tujuan= " + kota[idx])
    print(">>> Jarak         = " + str(jarak[idx]) + "km")
    print(">>> Ongkir per KM = Rp. " + str(ongkirperkm[idx])) 
    
    #hitung transaksi
    #fixjarak = jarak[idx]
    #fixongkirkm = ongkirperkm[idx]
    #totongkir = fixjarak * fixongkirkm

    fixjarak = jarak[idx]
    fixongkirkm = ongkirperkm[idx]
    totongkir = int(fixjarak) * int(fixongkirkm)    

    #Tampilkan total ongkir
    print(">>>-------------------------------------")
    print(">>> Total Biaya      =Rp. " + str(totongkir))
    Jwb = input(" >>> Apakah Anda ingin memulai program ulang ? y/t :  ")
    if Jwb == "t" or Jwb == "T":
        break