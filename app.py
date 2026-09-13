import plotly.express as px
import pandas as pd

données = pd.read_csv("ventes.csv")

# Pour chaque ligne, on calcule le chiffre d'affaires.
données["ca"] = données["prix"] * données["qte"]

# Question 6

# Valeurs par produit
ca_par_produit = données.groupby("produit")["ca"].sum()
print("Chiffre d'affaires par produit :", ca_par_produit)

ca_moyen_par_produit = données.groupby("produit")["ca"].mean()
print("Chiffre d'affaires moyen par produit :", ca_moyen_par_produit)

ca_median_par_produit = données.groupby("produit")["ca"].median()
print("Chiffre d'affaires médian par produit :", ca_median_par_produit)

ventes_par_produit = données.groupby("produit")["qte"].sum()
print("Quantités vendues par produit :", ventes_par_produit)

quantite_moyenne_par_produit = données.groupby("produit")["qte"].mean()
print("Quantité moyenne vendue par produit :", quantite_moyenne_par_produit)

quantite_mediane_par_produit = données.groupby("produit")["qte"].median()
print("Quantité médiane vendue par produit :", quantite_mediane_par_produit)

ecart_type_par_produit = données.groupby("produit")["qte"].std()
print("Écart-type des quantités par produit :", ecart_type_par_produit)

variance_par_produit = données.groupby("produit")["qte"].var()
print("Variance des quantités par produit :", variance_par_produit)

# Question 7 : voir le fichier question7.py.

# Question 8
figure_ventes_par_produit = px.pie(
    values=ventes_par_produit.values,
    names=ventes_par_produit.index,
    title="Quantités vendues par produit",
)
figure_ventes_par_produit.write_html("ventes-par-produit.html")

figure_ca_par_produit = px.pie(
    values=ca_par_produit.values,
    names=ca_par_produit.index,
    title="Chiffre d'affaires par produit",
)
figure_ca_par_produit.write_html("ca-par-produit.html")

ventes_par_region = données.groupby("region")["qte"].sum()
figure_ventes_par_region = px.pie(
    values=ventes_par_region.values,
    names=ventes_par_region.index,
    title="Quantités vendues par région",
)
figure_ventes_par_region.write_html("ventes-par-region.html")

print("Les trois graphiques HTML ont été générés avec succès.")
