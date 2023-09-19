def gallonat_litroiksi(gallona_maara):
    litra_maara = gallona_maara * 3.785
    return litra_maara

def main():
    while True:
        try:
            gallona_maara = float(input("Syötä bensiinin määrä gallonoina (negatiivinen lopettaa ohjelman): "))
            if gallona_maara < 0:
                print("Ohjelma lopetettu.")
                break
            litra_maara = gallonat_litroiksi(gallona_maara)
            print(f"{gallona_maara} gallonia on {litra_maara} litraa.")
        except ValueError:
            print("Virheellinen syöte. Syötä luku.")

if __name__ == "__main__":
    main()