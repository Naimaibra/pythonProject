
oikea_kayttajatunnus = "python"
oikea_salasana = "rules"
yritykset = 0

while yritykset < 5:
    kayttajatunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")

    if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty. Liian monta yritystä.")





