from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def hae_koordinaatit(icao_koodi):
    geolocator = Nominatim(user_agent="lentokenttien_etaisyys_laskuri")
    sijainti = geolocator.geocode(icao_koodi)
    if sijainti:
        return sijainti.latitude, sijainti.longitude
    else:
        return None

def laske_etaisyys(icao_koodi1, icao_koodi2):
    koordinaatit1 = hae_koordinaatit(icao_koodi1)
    koordinaatit2 = hae_koordinaatit(icao_koodi2)

    if koordinaatit1 is None or koordinaatit2 is None:
        return None



    etaisyys = geodesic(koordinaatit1, koordinaatit2).kilometers
    return etaisyys


if __name__ == "__main__":
    icao_koodi1 = input("Anna ensimmäinen lentokentän ICAO-koodi: ").strip().upper()
    icao_koodi2 = input("Anna toinen lentokentän ICAO-koodi: ").strip().upper()

    etaisyys = laske_etaisyys(icao_koodi1, icao_koodi2)

    if etaisyys is not None:
        print(f"Lentokenttien {icao_koodi1} ja {icao_koodi2} välinen etäisyys on {etaisyys:.2f} kilometriä.")
    else:
        print("Yksi tai molemmat lentokenttäkoodit eivät ole kelvollisia.")