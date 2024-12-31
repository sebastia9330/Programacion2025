Consulta del día #6: Práctica
Tarea:

1. Calcula el total de ventas por cada cliente usando una subconsulta en el bloque SELECT.
2. Muestra el ID del cliente, su nombre, y el monto total de ventas.
3. Ordena los resultados por el monto total en orden descendente.


SELECT ID_CLIENTE, NOMBRE, (SELECT SUM(VENTAS)
                            FROM VENTAS V
                            WHERE V.ID_CLIENTE = C.ID_CLIENTE) AS TOTAL_VENTA
FROM CLIENTE C
ORDER BY TOTAL_VENTA DESC;


--Corrección
SELECT C.ID_CLIENTE, 
        C.NOMBRE, 
        SUM(V.MONTO) AS TOTAL_VENTA
FROM CLIENTE C
LEFT JOIN VENTAS V ON C.ID_CLIENTE = V.ID_CLIENTE
GROUP BY C.ID_CLIENTE, C.NOMBRE
ORDER BY TOTAL_VENTA DESC;
