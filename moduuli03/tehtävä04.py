import random

# Arvotaan satunnainen luku väliltä 1..10
arvottu_luku = random.randint(1, 10)

yritykset = 0  # Pelaajan yritysten laskuri

while True:
    arvaus = int(input("Arvaa luku väliltä 1..10: "))
    yritykset += 1

    if arvaus < arvottu_luku:
        print("Liian pieni arvaus.")
    elif arvaus > arvottu_luku:
        print("Liian suuri arvaus.")
    else:
        print(f"Oikein! Arvasit luvun {arvottu_luku} {yritykset} yrityksellä.")
        break





