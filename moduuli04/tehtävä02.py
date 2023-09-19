
#Aloitetaan tyhjä lista, johon tallennetaan käyttäjän syöttämät luvut
numerot = []

# Kysytään käyttäjältä lukuja siihen saakka, kunnes tyhjä merkkijono syötetään
while True:
    syote = input("Syötä luku (tyhjä rivi lopettaa): ")

    if syote == "":

         break

    try:
        luku = float(syote)  # Yritetään muuttaa syöte luvuksi
        numerot.append(luku)  # Lisätään luku listaan
    except ValueError:
        print("Virheellinen syöte. Syötä luku tai tyhjä rivi lopettaaksesi.")

# Tarkistetaan, onko käyttäjän syöntti vähintään viisi lukua
if len(numerot) < 5:
    print("Syötit liian vähän lukuja.")
else:
    numerot.sort(reverse=True)

    # Tulostetaan viisi suurinta lukua
    print("Viisi suurinta lukua:")
    for i in range(5):
        print(numerot[i])
'''''

kapu