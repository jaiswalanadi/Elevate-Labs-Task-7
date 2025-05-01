SELECT productline AS product,
       SUM(quantityordered) AS total_qty,
       SUM(quantityordered * priceeach) AS revenue
FROM sales
GROUP BY productline
