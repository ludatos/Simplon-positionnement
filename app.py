import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

#Pour chaque ligne, on calcul une nouvelle colonne ca
données["ca"] = données["prix"] * données["qte"]

############# Question 6 ###########

#Valeurs par produit
caParProduit = données.groupby("produit")["ca"].sum()
print('Chiffre d''affaire par produit : ', caParProduit)

caMoyenParProduit = données.groupby("produit")["ca"].mean()
print('Chiffre d''affaire moyen par produit : ', caMoyenParProduit)

caMedianParProduit = données.groupby("produit")["ca"].median()
print('Chiffre d''affaire median par produit : ', caMedianParProduit)

venteParProduit = données.groupby("produit")["qte"].sum()
print('Ventes par produit : ', venteParProduit)

ecartTypeParProduit = données.groupby("produit")["qte"].std()
print('Ecart type des ventes par produit : ', ecartTypeParProduit)

varianceParProduit = données.groupby("produit")["qte"].var()
print('Variance des ventes par produit : ', varianceParProduit)

############# Question 7 ###########
#### Voir fichier question7.py #####

############# Question 8 ###########
figure_vente_par_produit = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')
figure_vente_par_produit.write_html('ventes-par-produit.html')

figure_ca_par_produit = px.pie(données, values='ca', names='produit', title='quantité vendue par produit')
figure_ca_par_produit.write_html('ca-par-produit.html')


############
figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')
