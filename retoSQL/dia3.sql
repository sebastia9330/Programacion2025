Tabla empleados:

id_empleado	nombre	departamento	salario	edad
1	        Carlos	Ventas	        3000	28
2	        Ana	Marketing	3500	32
3	        María	Ventas	        2500	24
4	        Pedro	Ventas	        4000	45
5	        Laura	Marketing	3000	29

/*
Consulta del día #3: Práctica
Tarea: Usando la tabla empleados como base:

1. Muestra el nombre y el salario de cada empleado.
2. Añade una columna que indique el salario más alto de su departamento.
3. Ordena los resultados por departamento y luego por salario en orden descendente.
*/

SELECT E1.NOMBRE, 
        E1.SALARIO, 
        (SELECT MAX(SALARIO)
        FROM EMPLEADOS E2
        WHERE E2.DEPARTAMENTO = E1.DEPARTAMENTO) AS SALARIO_MAYOR
FROM EMPLEADOS E1
ORDER BY E1.SALARIO DESC;
