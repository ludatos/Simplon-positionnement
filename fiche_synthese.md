# Fiche de synthèse - Positionnement

## Résultats d’analyse obtenus

### 3.a Le chiffre d'affaires total

```sql
SELECT SUM(prix * qte) AS chiffre_affaires_total
FROM ventes;
```

Le chiffre d'affaires total réalisé sur la période est de **44 825 €**.

### 3.b Les ventes par produit

#### Chiffre d'affaires par produit

```sql
SELECT produit, SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY produit;
```

| Produit | Chiffre d'affaires |
|---|---:|
| Produit A | 17 500 € |
| Produit B | 15 825 € |
| Produit C | 11 500 € |

#### Quantités vendues par produit

```sql
SELECT produit, SUM(qte) AS quantite_vendue
FROM ventes
GROUP BY produit;
```

| Produit | Quantité vendue |
|---|---:|
| Produit A | 1 750 unités |
| Produit B | 1 055 unités |
| Produit C | 575 unités |

Le Produit A est le plus vendu avec **1 750 unités**.  
Le Produit C est le moins vendu avec **575 unités**.  
Même si le Produit A est le plus vendu en volume, son chiffre d'affaires est proche de celui du Produit B car le prix unitaire du Produit B est plus élevé.

### 3.c Les ventes par région

#### Chiffre d'affaires par région

```sql
SELECT region, SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY region;
```

| Région | Chiffre d'affaires |
|---|---:|
| Nord | 20 725 € |
| Sud | 24 100 € |

#### Quantités vendues par région

```sql
SELECT region, SUM(qte) AS quantite_vendue
FROM ventes
GROUP BY region;
```

| Région | Quantité vendue |
|---|---:|
| Nord | 1 605 unités |
| Sud | 1 775 unités |

La région Sud génère le chiffre d'affaires le plus élevé avec **24 100 €** et possède également le volume des ventes le plus important avec **1 775 unités**.

### 6. Analyse avec Pandas

Les statistiques suivantes sont calculées pour chaque produit. L'écart-type et la variance correspondent aux valeurs d'échantillon calculées par défaut par Pandas.

| Produit | CA moyen | CA médian | Quantité moyenne | Quantité médiane | Écart-type des quantités | Variance des quantités |
|---|---:|---:|---:|---:|---:|---:|
| Produit A | 1 250,00 € | 1 225,00 € | 125,00 | 122,50 | 38,08 | 1 450,00 |
| Produit B | 1 217,31 € | 1 200,00 € | 81,15 | 80,00 | 21,23 | 450,64 |
| Produit C | 958,33 € | 900,00 € | 47,92 | 45,00 | 17,90 | 320,27 |

Le Produit A obtient le chiffre d'affaires moyen et le volume moyen les plus élevés. Ses ventes sont aussi les plus dispersées, comme l'indiquent son écart-type et sa variance supérieurs à ceux des autres produits.

### 7. Produit le plus vendu et le moins vendu

Le calcul réalisé en Python natif, sans utiliser Pandas, donne les résultats suivants :

- **Produit le plus vendu : Produit A, avec 1 750 unités.**
- **Produit le moins vendu : Produit C, avec 575 unités.**
