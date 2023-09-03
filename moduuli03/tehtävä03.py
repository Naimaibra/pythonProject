
# Alustetaan tyhjä lista saaduille luvuille

numerot = []

while True:
    syote = input("Syötä luku (tyhjä merkkijono lopettaa): ")

    if syote == "":
        break  # Lopetetaan silmukka, jos käyttäjä syöttää tyhjän merkkijonon

    try:
        luku = float(syote)  # Muunnetaan syöte liukuluvuksi
        numerot.append(luku)  # Lisätään luku listaan
    except ValueError:
        print("Virheellinen syöte. Syötä luku tai tyhjä merkkijono.")

if numerot:
    pienin = min(numerot)
    suurin = max(numerot)
    print(f"Pienin syöttämäsi luku oli {pienin} ja suurin oli {suurin}.")
else:
    print("Et syöttänyt yhtään lukua.")