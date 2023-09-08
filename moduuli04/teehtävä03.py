def onko_alkuluku(luku):
    if luku < 2:
        return False  # Luvut pienempiä kuin 2 eivät ole alkulukuja

    for i in range(2, luku):
        if luku % i == 0:
            return False  # Luku ei ole alkuluku, jos se on jaollinen jollakin muulla kuin 1 ja itsellään

    return True  # Luku on alkuluku, jos se ei ole jaollinen millään muulla kuin 1 ja itsellään


try:
    syote = int(input("Syötä kokonaisluku: "))

    if syote < 0:
        print("Negatiiviset luvut eivät voi olla alkulukuja.")
    elif onko_alkuluku(syote):
        print(f"{syote} on alkuluku.")
    else:
        print(f"{syote} ei ole alkuluku.")
except ValueError:
    print("Virheellinen syöte. Syötä kokonaisluku.")