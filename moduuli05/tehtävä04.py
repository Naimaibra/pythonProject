
def laske_summa(lista):
    summa = sum(lista)
    return summa

def main():
    # tehdään lista kokonaisluvuista testausta varten
    luku_lista = [1, 2, 3, 4, 5]

    # Kutsu funktiota ja tulosta palautettu summa
    summa = laske_summa(luku_lista)
    print(f"Listan summa on: {summa}")

if __name__ == "__main__":
    main()