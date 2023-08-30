# Kysytään käyttäjältä kuhan pituus senttimetreinä
kuha_pituus = float(input("Syötä kuhan pituus senttimetreinä: "))

# Alamittainen kuha on alle 37 cm
alamitta = 37

# Tarkistetaan, onko kuha alamittainen
if kuha_pituus < alamitta:
    puuttuvat_sentit = alamitta - kuha_pituus
    print(f"Kuha on alamittainen. Puuttuvia senttejä alimmasta sallitusta pyyntimitasta on {puuttuvat_sentit:.2f} cm.")
else:
    print("Kuha on riittävän iso. Voit pitää sen.")