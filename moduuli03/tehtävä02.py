# kitjoittaa ohjelma joka
hyttiluokka = input("Syötä hyttiluokka (LUX, A, B, C): ") .upper()

if hyttiluokka == "LUX":
    kuvaus = "parvekkeellinen hytti yläkannella"
elif hyttiluokka == "A":
    kuvaus = "ikkunallinen hytti autokannen yläpuolella"
elif hyttiluokka == "B":
    kuvaus = "ikkunaton hytti autokannen yläpuolella"
elif hyttiluokka == "C":
    kuvaus = "ikkunaton hytti autokannen alapuolella"
else:
    kuvaus = "Tuntematon hyttiluokka"

print(f"{hyttiluokka} on {kuvaus}.")