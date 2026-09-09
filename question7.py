import csv

fichier_csv = 'ventes.csv'

quantites_par_produit = {}

with open(fichier_csv, mode='r', encoding="utf-8-sig", newline="") as fichier:
    lecteur = csv.DictReader(fichier,delimiter=",")

    for ligne in lecteur:
        produit = ligne["produit"].strip()
        quantite = int(ligne["qte"])

        if produit in quantites_par_produit:
            quantites_par_produit[produit] += quantite
        else:
            quantites_par_produit[produit] = quantite

print("Quantités vendues par produit :")

for produit, quantite_totale in quantites_par_produit.items():
    print(f" {produit} : {quantite_totale}")

########### Comparaison des produits pour trouver le produit le plus vendu et le moins vendu
produit_plus_vendu = None
produit_moins_vendu = None
quantite_max = 0
quantite_min = None

for produit in quantites_par_produit:
    quantite = quantites_par_produit[produit]
    if quantite > quantite_max:
        quantite_max = quantite
        produit_plus_vendu = produit
    if quantite_min is None or quantite < quantite_min:
        quantite_min = quantite
        produit_moins_vendu = produit

print("Produit le plus vendu : ", produit_plus_vendu)
print("Produit le moins vendu : ", produit_moins_vendu)