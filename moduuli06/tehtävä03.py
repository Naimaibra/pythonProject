lentoasemat = {}

while True:
    print("Valitse toiminto:")
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")

    valinta = input("Syötä valinnan numero (1/2/3): ")

    if valinta == '1':
        icao_koodi = input("Syötä lentoaseman ICAO-koodi: ").strip().upper()
        nimi = input("Syötä lentoaseman nimi: ").strip()

        lentoasemat[icao_koodi] = nimi
        print(f"Lentoasema {icao_koodi} tallennettu nimellä {nimi}.")

    elif valinta == '2':
        icao_koodi = input("Syötä lentoaseman ICAO-koodi: ").strip().upper()

        if icao_koodi in lentoasemat:
            nimi = lentoasemat[icao_koodi]
            print(f"Lentoaseman {icao_koodi} nimi on {nimi}.")
        else:
            print(f"Lentoasemaa {icao_koodi} ei löydy tietokannasta.")

        elif valinta == '3':
        print("Ohjelma päättyy.")
        break

    else:
        print("Virheellinen valinta. Syötä 1, 2 tai 3.")