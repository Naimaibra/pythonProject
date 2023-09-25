
import requests

def hae_lentokentat(maakoodi):
    url = f"https://airport-info.p.rapidapi.com/airports?iso_country={maakoodi}"

    headers = {
        "X-RapidAPI-Host": "airport-info.p.rapidapi.com",
        "X-RapidAPI-Key": "SINUN_RAPIDAPI_AVAIN_TÄHÄN"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Lentokenttätietojen hakeminen epäonnistui.")
        return None

    def laske_lentokentat_tyypeittain(lentokentat):
        tyyppien_lukumaarat = {}

    for lentokentta in lentokentat:
            tyyppi = lentokentta["type"]
            if tyyppi in tyyppien_lukumaarat:
                tyyppien_lukumaarat[tyyppi] += 1
            else:
                tyyppien_lukumaarat[tyyppi] = 1

    return tyyppien_lukumaarat

    def main():
        maakoodi = input("Anna maakoodi (esim. FI): ")

    lentokentat = hae_lentokentat(maakoodi)

    if lentokentat:
        tyyppien_lukumaarat = laske_lentokentat_tyypeittain(lentokentat)

    print(f"\nLentokentät maassa {maakoodi} tyypeittäin:")
    for tyyppi, lukumaara in tyyppien_lukumaarat.items():
        print(f"{tyyppi}: {lukumaara} kappaletta")

if __name__ == "__main__":
    main()
