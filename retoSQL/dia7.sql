Consulta del día #7: Práctica
Tarea:

1. Encuentra los productos cuyo precio sea mayor al promedio de su categoría.
2. Incluye en la consulta una columna adicional con el ranking de los precios dentro de su categoría.
3. Muestra el ID del producto, el nombre, la categoría, el precio, y su ranking dentro de la categoría.
4. Ordena los resultados por categoría y ranking.

SELECT ID_PRODUCTO, NOMBRE, PRECIO, CATEGORIA, RANK() OVER(ORDER BY CATEGORIA DESC) AS RANKING
FROM PRODUCTOS
WHERE PRECIO > (SELECT AVG(PRECIO) FROM PRODUCTOS);


--Corrección
SELECT ID_PRODUCTO, 
        NOMBRE, 
        PRECIO, 
        CATEGORIA, 
        RANK() OVER(PARTITION BY CATEGORIA ORDER BY PRECIO DESC) AS RANKING
FROM PRODUCTOS
WHERE PRECIO > (SELECT AVG(PRECIO) 
                FROM PRODUCTOS P2 
                WHERE P2.CATEGORIA = PRODUCTOS.CATEGORIA);
