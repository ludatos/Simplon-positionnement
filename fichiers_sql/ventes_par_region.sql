SELECT region, SUM(qte) AS quantite_vendue
FROM ventes
GROUP BY region;
