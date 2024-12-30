Tabla empleados:

id_empleado	nombre	departamento	salario	edad
1	        Carlos	Ventas	        3000	28
2	        Ana	    Marketing	    3500	32
3	        María	Ventas	        2500	24
4	        Pedro	Ventas	        4000	45
5	        Laura	Marketing	    3000	29

Consulta del día #4: Práctica
Tarea: Usando la tabla empleados:

1. Muestra el nombre, el departamento y el salario de cada empleado.
2. Añade una columna que indique el número de empleados con salario mayor o igual al empleado actual dentro de su departamento.
3. Ordena el resultado por departamento y salario en orden descendente.

SELECT NOMBRE, DEPARTAMENTO, SALARIO
    SUM() OVER(PARTITION BY DEPARTAMENRO ORDER BY SALARIO DESC) as suma_salario
FROM EMPLEADOS
ORDER BY departamento desc;


--CORRECCION
SELECT NOMBRE, 
        DEPARTAMENTO, 
        SALARIO,
        SUM(SALARIO) OVER (PARTITION BY DEPARTAMENTO ORDER BY SALARIO DESC) AS suma_salario
FROM EMPLEADOS
ORDER BY DEPARTAMENTO DESC, SALARIO DESC;
