import random

# Arvotaan kolmenumeroisen koodin numerot (0..9)
kolmenumero_koodi = "".join(str(random.randint(0, 9)) for _ in range(3))

# Arvotaan nelinumeroisen koodin numerot (1..6)
nelinumero_koodi = "".join(str(random.randint(1, 6)) for _ in range(4))

# Tulostetaan koodit
print("Kolmenumero koodi:", kolmenumero_koodi)
print("Nelinumero koodi:", nelinumero_koodi)
