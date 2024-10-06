EUR_USD = 1.0800
EUR_GBP = 0.84663

print("Tämä ohjelma laskee valuuttamuunnoksia.")

eurot = float(input("Anna rahan määrä euroina: "))

dollarit = eurot * EUR_USD
punnat = eurot * EUR_GBP

print("Antamasi", format(eurot, '.2f'), "euroa muutettuna Yhdysvaltain dollareiksi on", end=" ", sep=" ")
print('{0:.2g}'.format(dollarit), "dollaria", end=" ",sep=" ")
print("ja Britannian punniksi", format(punnat, '.2f'), "puntaa.",sep=" ", end="\n")
print("Kiitos ohjelman käytöstä.")
