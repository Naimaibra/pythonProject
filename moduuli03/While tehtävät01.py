print("Muisti on leikkisilta tuulella ja haukkuu kokoajan")

kerrat = int(input("montako kartaa musti haukuu, anna luku:\n"))
tehty_haukut = 0


# 0 <5
while tehty_haukut < kerrat:
    print((" musti haukkuu woof woof"))
    #tehty_haukut = tehty_haukut + 1
    tehty_haukut += 1
    print("woof\n")

print("musti on nyt riehokas ja haukuu koko ajan. voit keskeä sitä lopetamaan")
kesky = input("Anna kesky, jos annat (stop) musti lopetaa haukuttamisen\n")

while kesky != "stop":
    kerrat = 0
    while kerrat < 10:
        print("musti haukuu WOOF WOOOF")
        kerrat += 1
        
    print("Musti haukuu WOOF FOOF")
    print("Musti haukuu WOOF FOOF")
    print("Musti haukuu WOOF FOOF")
    print("Musti haukuu WOOF FOOF")
    print("Musti haukuu WOOF FOOF")
    print("Musti haukuu WOOF FOOF")
    print("Musti haukuu WOOF FOOF")
    print("Musti haukuu WOOF FOOF")
    kesky = input("Anna kesky, jos annat (stop) musti lopettaa haukkuttamisen\n")
