while True:
    tuumat = float(input("Syötä tuumat (negatiivinen luku lopettaa ohjelman): "))

    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break

    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {senttimetrit} senttimetriä.")