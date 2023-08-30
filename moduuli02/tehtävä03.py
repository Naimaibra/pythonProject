# Kysytään käyttäjältä biologinen sukupuoli
sukupuoli = input("Syötä sukupuoli (nainen/mies): ")

# Kysytään käyttäjältä hemoglobiiniarvo (g/l)
hemoglobiini = float(input("Syötä hemoglobiiniarvo (g/l): "))

# Tarkistetaan sukupuoli ja määritetään normaalialueet
if sukupuoli == "nainen":
    matala = 117
    korkea = 175
elif sukupuoli == "mies":
    matala = 134
    korkea = 195
else:
    print("Tuntematon sukupuoli.")
    exit()

# Tarkistetaan hemoglobiiniarvon tila
if hemoglobiini < matala:
    tila = "alhainen"
elif hemoglobiini <= korkea:
    tila = "normaali"
else:
    tila = "korkea"

# Tulostetaan tulos
print(f"Hemoglobiiniarvo on {tila} sukupuolelle {sukupuoli}.")

