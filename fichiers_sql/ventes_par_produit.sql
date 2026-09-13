SELECT produit, SUM(qte) AS quantite_vendue
FROM ventes
GROUP BY produit;
