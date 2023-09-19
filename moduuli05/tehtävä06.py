def calculate_unit_price(diameter, price):
    pizzan_pinta_ala = 3.14159265359 * ((halkaisija / 2) ** 2)  # Calculate the area of the pizza
    yksikkohinta = hinta / pizzan_pinta_ala
    return yksikkohinta

def main():

    halkaisija1 = float(input("Syötä ensimmäisen pizzan halkaisija (cm): "))
    hinta1 = float(input("Syötä ensimmäisen pizzan hinta (€): "))

    halkaisija2 = float(input("Syötä toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Syötä toisen pizzan hinta (€): "))


    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)


    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta1 > yksikkohinta2:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat ovat saman hintaisia neliömetriä kohti.")


if __name__ == "__main__":
    main()