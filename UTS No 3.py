# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 21:50:21 2021

@author: Dell
Pemilik Toko bahan bangunan UD. Subur memesan sebuah program kepada Anda untuk dapat menampilkan
beberapa bahan bangunan yang dijualnya pada komputer. Sehingga konsumen dapat memilih dan membeli
barang dalam jumlah yang diinginkannya dan mengetahui jumlah uang yang harus dibayarnya. Berikut daftar
bahan bangunan yang dijualnya:
a. Asbes Gelombang @ Rp60.000
b. Cat Tembok Dulux 1Galon @ Rp250.000
c. Cat Tembok Avian 1 Galon @ Rp350.000
d. Aquaproof 5 Kg @ Rp50.000
e. Seng 2mm @ Rp70.000
f. Spandeks 1mm @ Rp92.000
Pembeli akan diberikan potongan 5% bila total pembelian sebelum PPN bernilai minimal Rp 500.000
Dari seluruh total pembayaran tersebut akan dikenakan pajak PPN 2%.
"""
jwb="y"
while jwb == "y" or jwb == "Y":
    print("=======================================================")
    print("Transaksi Penjualan Toko Bahan Bangunan UD Subur ")
    print("=======================================================")
    print("Kode = a . Asbes Gelombang @ Rp 60000 ")
    print("Kode = b . Cat Tembok Dulux 1 Galon @ Rp 250000 ")
    print("Kode = c . Cat Tembok Avian 1 Galon @ Rp 350000 ")
    print("Kode = d . Aquaproof 5 Kg @ Rp 50000 ")
    print("Kode = e . Seng 2 mm @ Rp 70000 ")
    print("Kode = f . Spandeks 1 mm @ Rp 92000 ")
    print("=======================================================")
    
    nmbrg=['Asbes Gelombang','Cat Tembok Dulux 1 Galon','Cat Tembok Avian 1 Galon','Aquaproof 5 Kg','Seng 2 mm','Spandeks 1 mm','Barang Tidak Ada / Cek Huruf']
    hrgbrg=[60000,250000,350000,50000,70000,92000,0]
    pilihan=input(">>> Masukkan Kode Nama Nama Barang = ")
    
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
    elif pilihan== "f":
        idx = 5
    else:
        idx = 6
        
    jmlbrg=input(">>> Masukkan Jumlah Barang = ")
    
    #Cetak Tampil Layar
    print(">>> ==================================================")
    print(">>> ============= Rincian Penjualan ==================")
    print(">>> Nama Barang = " + nmbrg[idx])
    print(">>> Harga Barang =Rp.  " + str(hrgbrg[idx]))
    print(">>> Jumlah Barang = " + str(jmlbrg) + " Item")
    
    #Hitung Transaksi Diskon 5 %
    fixhrgbrg = hrgbrg[idx]
    fixjmlbrg = jmlbrg
    x = int(fixhrgbrg) * int(fixjmlbrg) * (5/100)
    
    if int(fixhrgbrg) * int(fixjmlbrg) >= 500000:
        totbyr = int((fixhrgbrg) * int(fixjmlbrg)) - x
    else :
        totbyr = int(fixhrgbrg) * int(fixjmlbrg)
    
    #Hitung PPN 2 %
    fixppn = int(totbyr) * (2/100)
    
    #Hitung All Bayar
    fixallbyr = int(totbyr) + int(fixppn)
    
    #Tampilkan Total Bayar dan All Bayar 
    print(">>> ================================================")
    print(">>> Total Bayar = Rp. " + str(totbyr))
    print(">>> PPN = Rp. " + str(fixppn))
    print(">>> Total All Bayar (Total Bayar + PPN) = " + str(fixallbyr))
    jwb = input(">>> Apakah Anda Ingin Memulai Program Ulang ? y/t : ")
    if jwb == "t" or jwb == "T" :
        break