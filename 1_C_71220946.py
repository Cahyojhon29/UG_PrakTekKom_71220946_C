#soal nomor 1
print ("===========================")
print ("Operasi Matematika")
print ("1. Jumlah      [+]")
print ("2. Kurang      [-]")
print ("3. Kali        [*]")
print ("4. Bagi        [/]")
#Rumus 
print ("===========================")
opsi = int(input("Pilihan Operasi (1/2/3/4) :"))
print ("===========================")
Bil1 = int(input("Masukkan Bilangan Pertama :"))
Bil2 = int(input("Masukkan Bilangan Kedua :"))
def jumlah (Bil1,Bil2):
    hasil = Bil1+Bil2
    return hasil
def kurang (Bil1,Bil2):
    hasil = Bil1-Bil2
    return hasil
def kali (Bil1,Bil2):
    hasil = Bil1*Bil2
    return hasil
def bagi (Bil1,Bil2):
    hasil = Bil1/Bil2
    return hasil

if opsi == 1:
   print("Hasil operasi dari ",Bil1,"+",Bil2,"=",jumlah (Bil1,Bil2))
elif opsi == 2:
   print ("Hasil operasi dari ",Bil1,"-",Bil2,"=",kurang (Bil1,Bil2))
elif opsi == 3:
   print ("Hasil operasi dari ",Bil1,"*",Bil2,"=",kali (Bil1,Bil2))
elif opsi == 4:
   print ("Hasil operasi dari ",Bil1,"/",Bil2,"=",bagi (Bil1,Bil2))





