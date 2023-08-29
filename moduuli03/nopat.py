import random

noppa1 = noppa2 = heitot = 0 noppa1: 2  heitot: 6 noppa2: 4
while (noppa1 == 6 and noppa2 == 6):
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    heitot = heitot + 1
print(f"Tarvittiin {heitot:d} heittoa.")


