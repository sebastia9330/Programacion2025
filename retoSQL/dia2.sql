/*Consulta del día #2: Práctica
Tarea: Usando la tabla empleados como base:

Calcula el total de salarios por departamento.
Muestra únicamente los departamentos cuyo total de salarios sea mayor a 10,000.
Ordena los resultados por el total de salarios en orden descendente.*/

SELECT DEPARTAMENTO, SUM(SALARIO) AS TOTAL_SALARIOS
FROM EMPLEADOS
GROUP BY DEPARTAMENTO
HAVING SUM(SALARIO) > 10000
ORDER BY TOTAL_SALARIOS DESC;
