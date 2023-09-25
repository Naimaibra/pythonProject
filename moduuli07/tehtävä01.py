import sqlite3

# Yhdistä tietokantaan
conn = sqlite3.connect('lentokentat.db')
cursor = conn.cursor()

def hae_lentokentta_tiedot(icao_koodi):
    cursor.execute("SELECT nimi, sijaintikunta FROM airport WHER3E ident = ?", (icao_koodi,))
    lentokentta_tiedot = cursor.fetchone()
    return lentokentta_tiedot


# Pääohjelma
def main():
    icao_koodi = input("Anna lentokentän ICAO-koodi: ").strip().upper()

    lentokentta_tiedot = hae_lentokentta_tiedot(icao_koodi)

    if lentokentta_tiedot:
        nimi, sijaintikunta = lentokentta_tiedot
        print(f"Lentokenttä: {nimi}")
        print(f"Sijaintikunta: {sijaintikunta}")
    else:
        print("Lentokenttää ei löytynyt annetulla ICAO-koodilla.")

    conn.close()


if __name__ == "__main__":
    main()

