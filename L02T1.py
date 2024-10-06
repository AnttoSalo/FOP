Nimi = input("Kerro nimesi: ")
BensanHinta = float(input("Anna polttoaineen litrahinta desimaalilukuna: "))
TankatutLitrat = int(input(("Anna tankattujen litrojen määrä kokonaislukuna: ")))
KokonaisHinta = TankatutLitrat * BensanHinta
print(Nimi,"annoit polttoaineen litrahinnaksi",BensanHinta,"euroa ja tankattujen litrojen määräksi",TankatutLitrat,"litraa.")
print("Kokonaishinta on tällöin",KokonaisHinta,"euroa.")
print("Kiitos ohjelman käytöstä.")
