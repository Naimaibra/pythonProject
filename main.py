#Alla tulotetaan merkkijonoja
print("Morjst\nmatti")
print("mitä kuuluu")

# Sijoitetaan merkkijonoja muuttujaan name
name = "Viivi" + "virtanen"
age = 6 + 6
print(name)
# tulostetaan samalla print-komennolla
# tyyppimuunos 12 -> "12"
# age = str(age)
print(name + ",ikä:" + str(age))
# luetaan käyttäjältä syötä ja sijoittaa sen muutajaa
name = input("kuka olet?")
age = input("kuinka vanha olet?")
print("moi" + name+", olet" + age +"vuotta vanha." )
# muutetaan käyttäjän syötäja string kokonaisluvuksi (int) ja sijäitetään 1

print("vuoden päästä olet " + str(int(age) + 1) +" vuotta.")
#tyyppimuutos voidaan tehdä myös heti syötteen lukumisen yhteydässä:
# age = int(input("kuinka vanha olet? )

# jakolaskukone
num1 = int(input("Anna jaettava luku: "))
num2 = int(input("Anna jakaja: "))
result = num1 // num2
print("jakalaskun tulos: " + str(result)
print(f"jakolasku tulos:~{result:3f}")
print(f"pii")
