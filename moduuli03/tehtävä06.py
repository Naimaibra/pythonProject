def laske_pi(n):
    pisteet_ympyrassa = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            pisteet_ympyrassa += 1

    pi_likiarvo = 4 * pisteet_ympyrassa / n
    return pi_likiarvo


try:
    arvottavien_pisteiden_maara = int(input("Syötä arvottavien pisteiden määrä: "))

    if arvottavien_pisteiden_maara <= 0:
        print("Anna positiivinen luku.")
    else:
        pi_likiarvo = laske_pi(arvottavien_pisteiden_maara)
        print(f"Likimääräinen arvio piin arvosta: {pi_likiarvo}")
except ValueError:
    print("Virheellinen syöte. Anna positiivinen kokonaisluku arvottavien pisteiden määräksi.")