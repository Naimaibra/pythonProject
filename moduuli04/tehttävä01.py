import random

lukumaara = int(input("syötä arpakuutioiden lukumäärä: "))
summa = 0
#Käytetään for-silmukkaa heittämään kaikki arpakuutiot
for i in range(lukumaara):
    silmaluku = random.randint(1, 6)
    summa += silma luku
    print(f" heitto {i , 1}: {silmaluku}")
#Tulostetaan silmulukujen ja summa
print(f"kaikki heittojen summa : {summa}")

