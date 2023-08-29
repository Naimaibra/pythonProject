# yksi lieviska on 20 naulaa.
# yksi naula on 32 luotia.
# yksi luoti on 13,3 gramma.
"""
jotta saisi lasketua, joudut ensin selvitetään:i
kuinka monta naulaa leiviksiä on
kuinka monta luotia naulat on
nyt sinulla on läjä nauloja
"""
import math

leiviskät = float(input('Anna leiviskät: '))
naulat = float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))

# muutetaan grammoksi
mass_talent_g = telent * 20 * 32 * 13.3
mass_nais_g = nails * 32 * 13.3
mass_bullets_g = 13.3

mass_g = mass_nais_g + mass_nais_g + mass_bullets_g

# muutetaan kilogaramoiksi
mass_kg = mass_g / 1000

# eritellään desimaalit luvusta


result = math.modf(mass_kg)
result_kg = result[1]
result_g = result[0]

result_g = result + 1000

print("mass nynymittojen mukaan: ")
print(f"{result_kg:1,0f} kilogrammaa ja {result_g:1f,} grammaa")
