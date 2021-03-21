print('Print Character Pertama')
def digitAwal(x, y): 
    dasar = x
    eksponen = y
    pangkat = (x ** y)
    strPangkat = str(pangkat) #menguhbah output "pangkat" menjadi sring
    print('Character Pertamanya Adalah :', strPangkat[0])

x = int(input('Masukkan Angka : '))
y = int(input('Masukkan Angka : '))

digitAwal(x, y)
#masih bingung untuk membuat bukan user input
print('==========================================================')
print('Print Character Terakhir')
def digitAkhir(m, n): 
    dasar = m
    eksponen = n
    pangkat = (m ** n)
    strPangkat = str(pangkat) #menguhbah output "pangkat" menjadi sring
    print('Character Akhirnya Adalah :', strPangkat[-1])

m = int(input('Masukkan Angka : '))
n = int(input('Masukkan Angka : '))

digitAkhir(m, n)