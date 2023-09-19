# Luodaan tyhjä joukko nimiä varten
nimet = set()

while True:
    nimi = input("Syötä nimi (tyhjä rivi lopettaa): ")

    if not nimi:
        break  # Keskeytetään ohjelma, jos käyttäjä syöttää tyhjän merkkijonon

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

# Tulostetaan syötetyt nimet mielivaltaisessa järjestyksessä
print("Syötit seuraavat nimet:")
for nimi in nimet:
    print(nimi)