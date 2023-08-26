print("moikka")


# nimi = "naima"
nimi = input("mikä on sinun nimesi: ")

print("hei, sinun nimi on" + nimi)

input("anna ympyrän säde: ")

import math
radius = float (input("please give me the radius of the circle to calculate the area: "))
area = math.pi * (radius * radius)
print(f"the area is: {area}")
print(f"the area is: {area:5.2f}")



import math
#lasketaan suorakolmoinen kannan ja korkeus

A = float(input("Anna 1. kateetin pituus:"))
B = float(input("Anna 2. kateetin pituus:"))

# laskee hypotenuus
C = math.sqrt(A**2 + B**2)
print(C)

print("Hypotenuus pituus on",C)



