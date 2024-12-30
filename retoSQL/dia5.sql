Consulta del día #5: Práctica
Tarea:
Usando una subconsulta correlacionada:

1. Muestra el nombre de los productos cuyo precio es superior al precio promedio de los productos en la misma categoría.
2. Añade una columna que indique la categoría del producto.
3. Ordena los resultados por categoría y precio de mayor a menor.


SELECT id_PRODUCTO, NOMBRE, categoria
from productos p1
where precio > (SELECT AVG(PRECIO)
                FROM PRODUCTOS P2
                WHERE P2.ID_PRODUCTO = P1.ID_PRODUCTO);


--Correccion
SELECT ID_PRODUCTO, 
        NOMBRE, 
        CATEGORIA, 
        PRECIO
FROM PRODUCTOS P1
WHERE PRECIO > (SELECT AVG(PRECIO)
                FROM PRODUCTOS P2
                WHERE P2.CATEGORIA = P1.CATEGORIA)
ORDER BY CATEGORIA ASC, PRECIO DESC;
