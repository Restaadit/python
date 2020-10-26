uang = int(input('Masukkan Uang Anda : '))
print('Anda Memiliki Uang Sebesar ' + str(uang) )
buah = {'apel': 50000, 'mangga': 40000, 'jeruk': 30000} 

for nama_buah in buah:
    print('----------------------------------------------------------')
    print('Harga ' + nama_buah + ' ' + str(buah[nama_buah]) + ' Rupiah Per Kilo')
    
    jbuah = int(input('Mau berapa Kilo' + nama_buah + ' ?:'))
    print('Anda membeli ' + str(jbuah) + ' Kilo ' + nama_buah)

    total_harga = buah[nama_buah] * jbuah 
    print('Harga total adalah ' + str(total_harga) + ' Rupiah')

    if uang >= total_harga:
        print('Anda telah membeli ' + str(jbuah) + ' Kilo ' + nama_buah)
        uang -= total_harga

        if uang == 0:
            print('Uang Anda telah habis')
            break
    else:
        print('Uang Anda tidak mencukupi')
        print('Anda tidak dapat membeli ' + nama_buah + ' sebanyak itu')

print('Uang Anda tinggal ' + str(uang) + ' Rupiah')