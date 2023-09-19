import random

def heita_noppaa():
    return random.randint(1, 6)


def main():
    heittojen_maara = 0
    while True:
        heitto = heita_noppaa()
        print(f"Heitto {heittojen_maara + 1}: {heitto}")
        heittojen_maara += 1
        if heitto == 6:
            break

    print(f"Kuutonen saatiin heitolla {heittojen_maara}!")

if __name__ == "__main__":
    main()

