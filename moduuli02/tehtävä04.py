# kysytään käyttäjältä biologisen sukupuolen ja hemoglobiiniarvon (g/l)

sukupuoli = input("Mikä on biologinen sukupuolisi? (mies/nainen): ")
hemoglobiini = float(input("Mikä on hemoglobiiniarvo (g/1)? "))
if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("hemoglobiiniarvo on alhainen. ")
    elif hemoglobiini >167:
        print("hemohlobiiniarvo on kervea.")
    else:
        print("hemohlobiini on normaali")
if sukupuoli == "nainen":
    if hemoglobiini <117:
        print("hemoglobiini on alhainen.")
    elif hemoglobiini >155:
        print("hemogloniini on korkea.")
    else:
        print("hemoglobiini on normaali.")

else:
print("syöte on virheellinen.")