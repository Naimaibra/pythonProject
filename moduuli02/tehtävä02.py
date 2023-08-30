# Kysytään käyttäjältä laivan hyttiluokka
hyttiluokka = input("Syötä laivan hyttiluokka (LUX, A, B, C): ")

# Tarkistetaan hyttiluokka ja tulostetaan sen kuvaus
if hyttiluokka == "LUX":
    kuvaus = "parvekkeellinen hytti yläkannella."
elif hyttiluokka == "A":
    kuvaus = "ikkunallinen hytti autokannen yläpuolella."
elif hyttiluokka == "B":
    kuvaus = "ikkunaton hytti autokannen yläpuolella."
elif hyttiluokka == "C":
    kuvaus = "ikkunaton hytti autokannen alapuolella."
else:
    kuvaus = "Tuntematon hyttiluokka."

# Tulostetaan kuvaus
print(f"{hyttiluokka} on {kuvaus}")