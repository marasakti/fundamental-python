"""
Type Data Dictionary menghubungkan antara Key dan Value
KVP = Key Value Pair
Dictionary = Kamus atau Terjemahan
"""

kamus = {}
kamus ['Anak laki laki'] = 'Son'
kamus ['Istri'] = 'Wife'
kamus ['Ayah'] = 'Father'
kamus ['Ibu'] = 'Mother'
print(kamus)
print(kamus['Ayah'])
print(kamus['Ibu'])
#Hanya berlaku satu arah dan tidan berlaku sebaliknya, Jika ingin menerjemahkan bolak balik maka list data harus ditambah

print('\nData ini dikirimkan dari server untuk memberikan informasi tentang posisi driver')
data_server = {
    'tanggal': '2021-08-24',
    'driver_list': ['Eko', 'Dwi', 'Tri', 'Catur']
}
print(data_server)
print(f"Driver disekitar sini {data_server['driver_list' ]}")
#Ambil data pertama dari List
print(f"Driver #1 : {data_server['driver_list'][0]}")
#Ambil data Ketiga dari List
print(f"Driver #3 : {data_server['driver_list'][2]}")
#Menambah Keterangan Jarak dalam Hitungan Meter ke LIst driver
data_server = {
    'tanggal': '2021-08-24',
    'driver_list': [
        {'Nama': 'Eko', 'Jarak': '20'},
        {'Nama': 'Dwi', 'Jarak': '30'},
        {'Nama': 'Tri', 'Jarak': '40'},
        {'Nama': 'Catur', 'Jarak': '50'}
    ]
}
print("\nMenambah Keterangan Jarak dalam Hitungan Meter ke LIst driver")
#Ambil data pertama dari List
print(f"Driver #1 : {data_server['driver_list'][0]}")
#Ambil data Ketida dari List
print(f"Driver #3 : {data_server['driver_list'][2]}")
print('\nHanya Mengambil Jarak Driver')
print(f"Jarak Driver Pertama : {data_server['driver_list'][0]['Jarak']} meter")
print('\nHanya Mengambil Nama Driver')
print(f"Driver Pertama : {data_server['driver_list'][0]['Nama']}")