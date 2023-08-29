sukupuoli = int("mikä on biologinen sukupuoli? (nainen/ mies)")
sukupuoli = input("Syötä sukupuoli (Mies/Nainen): ").lower()
hemoglobiiniarvo = float(input("Syötä hemoglobiiniarvo (g/l): "))

if sukupuoli == "mies":
    alaraja = 134
    ylaraja = 195
elif sukupuoli == "nainen":
    alaraja = 117
    ylaraja = 175
else:
    print("Tuntematon sukupuoli")

if hemoglobiiniarvo < alaraja:
    tulos = "alhainen"
elif hemoglobiiniarvo >= alaraja and hemoglobiiniarvo <= ylaraja:
    tulos = "normaali"
else:
    tulos = "korkea"

print(f"Hemoglobiiniarvo on {tulos}.")








