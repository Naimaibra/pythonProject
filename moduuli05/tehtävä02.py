import random


def heita_noppaa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

def main():
    tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))
    maksimisilmaluku = int(input("Anna nopan maksimisilmäluku: "))

    heittojen_maara = 0
    while True:
        heitto = heita_noppaa(tahkojen_maara)
        print(f"Heitto {heittojen_maara + 1}: {heitto}")
        heittojen_maara += 1
        if heitto == maksimisilmaluku:
            break

    print(f"Nopan maksimisilmäluku {maksimisilmaluku} saatiin heitolla {heittojen_maara}!")

if __name__ == "__main__":
    main()