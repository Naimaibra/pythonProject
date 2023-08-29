# Kysytään käyttäjältä massat leivisköinä, nauloina ja luoteina
leiviskat = float(input("Syötä massa leivisköinä: "))
naulat = float(input("Syötä massa nauloina: "))
luodit = float(input("Syötä massa luoteina: "))

# Muunnetaan keskiaikaiset mitat kilogrammoiksi ja grammoiksi
# Yksi leiviskä on 20 naulaa, yksi naula on 32 luotia, ja yksi luoti on 13.3 grammaa
yhteismaara_luoteina = (leiviskat * 20 + naulat) * 32 + luodit
yhteismaara_grammoina = yhteismaara_luoteina * 13.3

# Muunnetaan grammat kilogrammoiksi ja grammoiksi
kilogrammat = yhteismaara_grammoina // 1000
grammat = yhteismaara_grammoina % 1000

# Tulostetaan tulokset
print(f"Kokonaismassa: {kilogrammat} kg {grammat} g")
