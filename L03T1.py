print("Anna kaksi kokonaislukua.")
Luku1 = int(input("Anna ensimmäinen luku: "))
Luku2 = int(input("Anna toinen luku: "))
print("\nSelvitetään kumpi luvuista on suurempi.")

Jakojaannos = str(Luku1 % Luku2)
Luku1Parillinen = "ei ole parillinen"
Luku2Parillinen = "ei ole parillinen"

if Luku1 % 2 == 0:
    Luku1Parillinen = "on parillinen"
if Luku2 % 2 == 0:
    Luku2Parillinen = "on parillinen"

if Luku1 > Luku2:
    Isompi = str(Luku1)
    Pienempi = str(Luku2)
    print("Luku", Isompi, "on suurempi kuin luku", Pienempi+"."+"\n")
elif Luku2 > Luku1:
    Isompi = str(Luku2)
    Pienempi = str(Luku1)
    print("Luku", Isompi, "on suurempi kuin luku", Pienempi+"."+"\n")
else:
    print("Luvut ovat yhtä suuria."+"\n")

print("Kun luku", Luku1, "jaetaan luvulla", str(Luku2) + ", jakojäännös on", Jakojaannos+"."+"\n")
print("Luku", Luku1, Luku1Parillinen+".")
print("Luku", Luku2, Luku2Parillinen+"."+"\n")

print("Kiitos ohjelman käytöstä.")
