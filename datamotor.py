import os
import random
import string

os.system("cls")  


print(f" {'DATA MOTOR ':#^35}")
data = dict()
while True:
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    
    NamaM = input("Enter nama Motor\t: ")
    Merek = input("Enter Motor (misal: Honda, Yamaha): ")
    Jenis = input("Enter Jenis\t: ")
    
    data[keyFinal] = {
        'NamaM': NamaM,
        'Merek': Merek,
        'Jenis': Jenis
    }

    opsi = input("input lagi (ya/t) : ").lower()
    if opsi == 't':
        break
  
# Menampilkan hasil data
print("-" * 40)
print(f"{'Key':<5} {'Nama Motor ':<20} {'Merek':<15} {'Jenis':<15}")
print("-" * 40)
for k, v in data.items():
    print(f"{k:<5} {v['Nama Motor']:<20} {v['Merek']:<15} {v['Jenis']:<15}")

# Menampilkan semua data
print("-" * 40)
print("Data Motor :")
print(data)