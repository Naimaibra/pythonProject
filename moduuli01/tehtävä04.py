# Kysytään käyttäjältä kolme kokonaislukua

luku1 = int(input("Syötä ensimmäinen kokonaisluku: "))
luku2 = int(input("Syötä toinen kokonaisluku: "))
luku3 = int(input("Syötä kolmas kokonaisluku: "))


# Lasketaan lukujen summa, tulo ja keskiarvo
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

# Tulostetaan tulokset
print(f"Lukujen summa: {summa}")
print(f"Lukujen tulo: {tulo}")
print(f"Lukujen keskiarvo: {keskiarvo}")