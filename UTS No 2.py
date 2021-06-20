# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:22:08 2021

@author: DELL
"""

jwb="y"
while  jwb =="y" or jwb =="Y":
    print("=========================================================")
    print("Transaksi Penjualan Oli Bengkel Motor UD Matahari ")
    print("=========================================================")
    print("Kode = a. Duration SW20 1L @ Rp 53000 ")
    print("Kode = b. Castrol Magnatec 1L @ Rp 50000 ")
    print("Kode = c. Federal Supreme XX 1L @ Rp 54000 ")
    print("Kode = d. Yamalube 1L @ Rp 45000 ")
    print("Kode = e. Shell 1L @ Rp 46000 ")
    print("=========================================================")
    
    nmoli=['Duration SW20 1L','Castrol Magnatec 1L','Federal SupremeXX 1L','Yamalube 1L','Shell 1L','Barang Tidak Ada / Cek Huruf']
    hrgoli=[53000,50000,54000,45000,46000,0]
    pilihan=input(">>> Masukkan Kode Nama Oli = ")
    #identifikasi pilihan
    if pilihan== "a":
        idx = 0
    elif pilihan== "b":
        idx = 1
    elif pilihan== "c":
        idx = 2
    elif pilihan== "d":
        idx = 3
    elif pilihan== "e":
        idx = 4
    else:
        idx = 5
    
    jmloli=input(">>> Masukkan Jumlah Oli = ")
    #Cetak Tampilan Layar
    print(">>> ======================================================")
    print(">>> ============ Rincian Penjualan =======================")
    print(">>> Pilihan Barang = " + nmoli[idx])
    print(">>> Harga Oli =Rp.  " + str(hrgoli[idx]))
    print(">>> Jumlah Oli = " + str(jmloli) + " Botol")
    print(">>> ======================================================")
    
    #hitung transaksi diskon 5 %
    fixhrgoli = hrgoli[idx]
    fixjmloli = jmloli
    x = int(fixhrgoli) * int(fixjmloli) * (5/100)
    
    if int(fixhrgoli) * int(fixjmloli) >= 200000:
        totbyr = int((fixhrgoli) * int(fixjmloli)) - x
    else :
        totbyr = (fixhrgoli) * int(fixjmloli) 
    
    #Hitung PPN 1 %
    fixppn = int(totbyr) * (1/100)
    
    #Hitung All Bayar
    fixallbyr = int(totbyr) + int(fixppn)
    
    #Tampilkan Total Bayar dan ALL Total Bayar
    print(">>> ======================================================")
    print(">>> Total Bayar = Rp. " + str(totbyr))
    print(">>> PPN = Rp. " + str(fixppn))
    print(">>> Total All Bayar (Total Bayar + PPN) = " + str(fixallbyr))
    jwb = input(">>>Apakah Anda Ingin Memulai Program Ulang ? y/t : ")
    if jwb == "t" or jwb == "T" :
        break