/*Consulta del día #1: Práctica
Tarea: Usando la tabla empleados como base:

1. Encuentra a los empleados cuyo salario es menor al promedio de la tabla.
2. Filtra solo a los empleados del departamento "Marketing".
3. Ordena los resultados por edad en orden ascendente.*/

SELECT NOMBRE, SALARIO
FROM EMPLEADOS
WHERE SALARIO < (SELECT AVG(SALARIO) FROM EMPLEADOS)
    AND DEPARTAMENTO = 'Marketing'
ORDER BY EDAD ASC;
