print('Ada Sebuah Keluarga Dengan 4 Orang Anak yang bernama :')
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\nTipe Data List / Daftar / Array')
anak = ['Eko', 'Dwi', 'Tri', 'Catur']
print(anak)
print('\nKemudian lahirlah Anak Kelima sehingga :')
anak.append('Lima')
print(anak)
print('\nSapa Anak ke - 3')
print(f'Hi {anak[2]}!')
print('\nSapa Anak ke - 5')
print(f'Hi {anak[4]}!')
print('\nSapa Anak Pertama')
print(f'Hi {anak[0]}!')
print('\nSapa Semua Anak')
for a in anak:
    print(f'Hi {a}!')
