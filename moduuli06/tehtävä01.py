
# Määritellään vuodenajat merkkijonoina monikkotietorakenteeseen
vuodenajat = ("talvi", "kevät", "kesä", "syksy", "talvi")

# Kysytään käyttäjältä kuukauden numero
kuukausi_numero = int(input("Syötä kuukauden numero (1-12): "))

# Tarkistetaan, että annettu kuukauden numero on kelvollinen
if 1 <= kuukausi_numero <= 12:

    vuodenaika_indeksi = (kuukausi_numero - 1) // 3
    vuodenaika = vuodenajat[vuodenaika_indeksi]
    print(f"Kuukausi {kuukausi_numero} kuuluu vuodenaikaan {vuodenaika}.")
else:
    print("Virheellinen kuukauden numero. Syötä numero väliltä 1-12.")