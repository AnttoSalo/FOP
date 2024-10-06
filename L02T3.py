print("Tämä ohjelma laskee tehtyjen ohjelmointitehtävien keskiarvon neljän opiskelijan tekemien tehtävien määristä.")
Opiskelija1 = int(input("Anna ensimmäisen opiskelijan tekemien tehtävien määrä: "))
Opiskelija2 = int(input("Anna toisen opiskelijan tekemien tehtävien määrä: "))
Opiskelija3 = int(input("Anna kolmannen opiskelijan tekemien tehtävien määrä: "))
Opiskelija4 = int(input("Anna neljännen opiskelijan tekemien tehtävien määrä: "))

Summa = Opiskelija1 + Opiskelija2 + Opiskelija3 + Opiskelija4
KeskiarvoPyoristetty = round(Summa / 4, 1)
KeskiarvoKokonaisluku = int(Summa / 4)

print("Antamiesi tehtyjen tehtävien summa on", str(Summa) + ".")
print("Antamiesi tehtyjen tehtävien keskiarvo on", str(KeskiarvoPyoristetty) + ".")
print("Keskiarvo on katkaistuna kokonaislukuna", str(KeskiarvoKokonaisluku) + ".")
print("Kiitos ohjelman käytöstä.")
