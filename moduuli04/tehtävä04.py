# Luodaan tyhjä lista kaupungeille
kaupungit = []

# Käytetään for-silmukkaa kaupunkien kysymiseen
for i in range(5):
    kaupunki = input(f"Syötä kaupunki {i+1}: ")
    kaupungit.append(kaupunki)

# Tulostetaan kaupunkien nimet allekkain
print("Kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)