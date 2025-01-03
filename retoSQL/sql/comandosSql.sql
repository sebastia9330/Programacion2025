/*################### CURSO SQL COMANDO POR COMANDO ##################*/

/*====================================================================*/
-- 1. CREATE DATABASE
-- COMANDO UTILIZADO PARA CREAR BASES DE DATOS
-- SINTAXIS
CREATE DATABASE NOMBRE_BASE_DE_DATOS;

/*====================================================================*/
-- 2. CREATE TABLE
-- COMANDO UTILIZADO PARA CREAR TABLAS
-- SINTAXIS
CREATE TABLE TABLA_ej(
    -- CAMPOS O COLUMNAS
    ID NUMBER(4),
    NOMBRE VARCHAR2(25),
    EDAD NUMBER(2),
    FECHA_NACIMIENTO DATE
);

/*====================================================================*/
-- 3. SELECT
-- COMANDO UTILIZADO PARA SELECCIONAR LOS CAMPOS QUE QUEREMOS VISUALIZAR
-- SINTAXIS
SELECT CAMPO1, CAMPO2
FROM NOMBRE_TABLA;
--EJEMPLO
SELECT ID_PRODUCTO, NOMBRE, PRECIO
FROM PRODUCTOS;

-- SINTAXIS PARA VISUALIZAR TODOS LOS CAMPOS
SELECT *
FROM NOMBRE_TABLA;

/*====================================================================*/
-- 4. DISTINCT
-- COMANDO USADO PARA SELECCIONAR LOS CAMPOS DISTINTOS
-- SINTAXIS
SELECT DISTINCT CAMPO
FROM NOMBRE_TABLA;
-- EJEMPLO
SELECT DISTINCT PRECIO
FROM PRODUCTOS

-- SINTAXIS PARA VISUALIZAR TODOS LOS CAMPOS
SELECT DISTINCT *
FROM NOMBRE_TABLA

/*====================================================================*/
-- 5. WHERE
-- COMANDO USADO PARA FILTRAR LOS REGISTROS BAJO UNA CONDICION ESPECIFICA
-- SINTAXIS
SELECT columnas
FROM tabla
WHERE condición;

-- Operadores comunes usados en WHERE:
-- Operadores de comparación:
    --=: Igual a.
    --<> o !=: Distinto de.
    -->: Mayor que.
    --<: Menor que.
    -->=: Mayor o igual que.
    --<=: Menor o igual que.

-- Operadores lógicos:
    --AND: Ambas condiciones deben cumplirse.
    --OR: Al menos una condición debe cumplirse.
    --NOT: Invierte la condición.

-- Operadores especiales:
    --BETWEEN: Especifica un rango.
    --IN: Busca un valor dentro de una lista.
    --LIKE: Busca patrones.
    --IS NULL: Verifica si un campo está vacío.

--Ejemplo práctico:
SELECT nombre, salario
FROM empleados
WHERE salario > 50000 AND departamento = 'Ventas';


/*====================================================================*/
-- 6. ORDER BY
-- COMANDO USADO PARA ORGANIZAR LOS REGISTROS YA SEA DE FORMAS ASCENDENTE O DESENDENTE
-- LOS REGISTROS POR DEFECTO VIENEN ORGANIZADOS DE FORMA ASCENDNETE
-- SINTAXIS
SELECT columnas
FROM tabla
ORDER BY columna1 [ASC | DESC], columna2 [ASC | DESC];

SELECT nombre, salario
FROM empleados
ORDER BY 2 DESC; -- Ordena por la segunda columna, es decir, salario.

/*====================================================================*/
-- 7. LIKE
-- La cláusula LIKE en SQL se utiliza para buscar patrones en una columna mediante el uso de caracteres comodín
-- SINTAXIS
SELECT columnas
FROM tabla
WHERE columna LIKE %patrón;
--EJEMPLO
SELECT NOMBRE
FROM PRODUCTOS
WHERE NOMBRE LIKE '%SA';


/*====================================================================*/
-- 8. AND.OR.NOT
-- NOT: Se utiliza para negar una condición. Si la condición es verdadera, el operador NOT la convierte en falsa, y viceversa.
-- SINTAXIS
SELECT columnas
FROM tabla
WHERE NOT condicion;
--EJEMPLO
SELECT *
FROM empleados
WHERE NOT departamento = 'Recursos Humanos';


-- AND: Se usa para combinar dos o más condiciones. Todas las condiciones deben ser verdaderas para que la expresión sea evaluada como verdadera.
-- SINTAXIS
SELECT columnas
FROM tabla
WHERE condicion1 AND condicion2;
--EJEMPLO
SELECT *
FROM empleados
WHERE salario > 5000 AND departamento = 'Ventas';


--OR: Permite combinar dos o más condiciones. Solo una de las condiciones debe ser verdadera para que la expresión sea evaluada como verdadera.
SELECT columnas
FROM tabla
WHERE condicion1 OR condicion2;
--EJEMPLO
SELECT *
FROM empleados
WHERE departamento = 'Ventas' OR departamento = 'Marketing';



/*====================================================================*/
-- 9. LIMIT
-- El comando LIMIT en SQL se utiliza para restringir el número de filas que devuelve una consulta
-- SINTAXIS
SELECT columnas
FROM tabla
[WHERE condición]
LIMIT número_de_filas;
--EJEMPLO
SELECT nombre, salario
FROM empleados
WHERE departamento = 'Ventas'
LIMIT 5;



/*====================================================================*/
-- 10. NULL, NOT NULL
-- En SQL, NULL se utiliza para representar valores desconocidos o faltantes en una base de datos.
-- SINTAXIS
SELECT columna1, columna2
FROM tabla
WHERE columna1 IS NULL;  -- Filtra filas donde columna1 tiene un valor nulo
--EJEMPLO
SELECT ID_PRODUCTO, NOMBRE
FROM PRODUCTOS
WHERE PRECIO IS NULL;

SELECT columna1, columna2
FROM tabla
WHERE columna1 IS NOT NULL;  -- Filtra filas donde columna1 no tiene un valor nulo
--EJEMPLO
SELECT ID_PRODUCTO, NOMBRE
FROM PRODUCTOS
WHERE PRECIO IS NOT NULL;


/*====================================================================*/
-- 11. MIN, MAX
-- Los comandos MIN y MAX en SQL se utilizan para obtener el valor mínimo o máximo de una columna en un conjunto de datos
-- SINTAXIS
SELECT MIN(columna)
FROM tabla
[WHERE condición];
--EJEMPLO
SELECT MIN(salario) AS salario_mínimo
FROM empleados
WHERE departamento = 'Ventas';


SELECT MAX(columna)
FROM tabla
[WHERE condición];
--EJEMPLO
SELECT MAX(salario) AS salario_máximo
FROM empleados
WHERE departamento = 'Marketing';


/*====================================================================*/
-- 12. COUNT
-- El comando COUNT en SQL se utiliza para contar el número de filas o valores en una columna
-- SINTAXIS
SELECT COUNT(*)
FROM tabla
[WHERE condición];
--EJEMPLO
SELECT COUNT(*)
FROM empleados
WHERE departamento = 'Ventas';


-- CONTAR TODAS LAS FILAS DE UNA TABLA
SELECT COUNT(*)
FROM empleados;


/*====================================================================*/
-- 13. SUM
-- SUM en SQL se usa para calcular la suma total de una columna numérica en un conjunto de registros.
-- SINTAXIS
SELECT SUM(columna)
FROM tabla
WHERE condición;
--EJEMPLO
SELECT SUM(salario)
FROM empleados
WHERE departamento = 'Ventas';



/*====================================================================*/
-- 14. AVG
-- El comando AVG en SQL se utiliza para calcular el promedio de una columna numérica en un conjunto de registros.
-- SINTAXIS
SELECT AVG(columna)
FROM tabla
WHERE condición;
--EJEMPLO
SELECT AVG(salario)
FROM empleados
WHERE departamento = 'Ventas';



/*====================================================================*/
-- 15. IN
-- El comando IN en SQL se utiliza para verificar si un valor específico se encuentra dentro de un conjunto de valores.
-- SINTAXIS
SELECT columna1, columna2, ...
FROM tabla
WHERE columna IN (valor1, valor2, valor3, ...);
--EJEMPLO
SELECT nombre, departamento
FROM empleados
WHERE departamento IN ('Ventas', 'Marketing', 'Finanzas');


/*====================================================================*/
--16. BETWEEN
-- El comando BETWEEN en SQL se usa para filtrar los resultados de una consulta dentro de un rango determinado.
-- SINTAXIS
SELECT columna1, columna2, ...
FROM tabla
WHERE columna BETWEEN valor1 AND valor2;
--EJEMPLO
SELECT nombre, salario
FROM empleados
WHERE salario BETWEEN 50000 AND 80000;


/*====================================================================*/
--17. AS
-- El comando AS en SQL se utiliza para asignar un alias a una columna o una tabla, lo que facilita la lectura y la escritura de consultas
-- SINTAXIS
SELECT columna AS alias
FROM tabla AS alias_tabla;
--EJEMPLO
SELECT nombre AS nombre_empleado, salario AS salario_anual
FROM empleados;


/*====================================================================*/
--18. CONCAT
--El comando CONCAT en SQL se utiliza para concatenar (unir) dos o más cadenas de texto en una sola.
-- SINTAXIS
CONCAT(cadena1, cadena2, ...)
--EJEMPLO
SELECT CONCAT(nombre, ' ', apellido) AS nombre_completo
FROM empleados;


/*====================================================================*/
-- 19. GROUP BY
-- El comando GROUP BY en SQL se utiliza para agrupar filas que tienen los mismos valores en columnas específicas. Es comúnmente usado en combinación con funciones de agregación como SUM(), AVG(), COUNT(), MAX(), MIN() para realizar cálculos en grupos de datos.
-- SINTAXIS
SELECT columna1, columna2, ..., función_agregada(columna)
FROM tabla
WHERE condición
GROUP BY columna1, columna2, ...;
--EJEMPLO COUNT
SELECT departamento, COUNT(*) AS numero_empleados
FROM empleados
GROUP BY departamento;
--EJEMPLO AVG
SELECT departamento, AVG(salario) AS salario_promedio
FROM empleados
GROUP BY departamento;


/*====================================================================*/
-- 20. HAVING
-- El comando HAVING en SQL se utiliza junto con GROUP BY para filtrar los resultados de una consulta después de que se han agrupado.
-- SINTAXIS
SELECT columna1, columna2, ..., función_agregada(columna)
FROM tabla
WHERE condición
GROUP BY columna1, columna2, ...
HAVING condición_de_agregación;
--EJEMPLO
SELECT departamento, COUNT(*) AS numero_empleados
FROM empleados
GROUP BY departamento
HAVING COUNT(*) > 5;


/*====================================================================*/
-- 21. CASE, WHEN, THEN
-- El comando CASE en SQL es utilizado para realizar evaluaciones condicionales dentro de una consulta, lo que permite devolver valores diferentes dependiendo de las condiciones que se cumplan.
-- SINTAXIS
SELECT columna1, 
    CASE columna2
        WHEN 'valor1' THEN 'Resultado1'
        WHEN 'valor2' THEN 'Resultado2'
        ELSE 'Resultado predeterminado'
    END AS resultado
FROM tabla;
--EJEMPLO
SELECT nombre, salario,
    CASE 
        WHEN salario < 30000 THEN 'Bajo'
        WHEN salario BETWEEN 30000 AND 60000 THEN 'Medio'
        ELSE 'Alto'
    END AS categoria_salario
FROM empleados;


/*====================================================================*/
-- 22. IFNULL
-- El comando IFNULL en SQL se utiliza para manejar valores NULL, reemplazándolos con un valor predeterminado especificado. Es comúnmente usado en MySQL.
-- SINTAXIS
IFNULL(expresión, valor_por_defecto)
--EJEMPLO
SELECT nombre, IFNULL(salario, 0) AS salario_ajustado
FROM empleados;


/*====================================================================*/
-- 23. INSERT
-- El comando INSERT en SQL se utiliza para agregar nuevos registros a una tabla en una base de datos.
-- SINTAXIS
INSERT INTO nombre_tabla (columna1, columna2, ..., columnaN)
VALUES (valor1, valor2, ..., valorN);
--EJEMPLO
INSERT INTO empleados (id_empleado, nombre, salario)
VALUES (1, 'Juan Pérez', 50000);
--EJEMPLO DE INSERCION CON UNA SUBCONSULTA
INSERT INTO empleados_activos (id_empleado, nombre)
SELECT id_empleado, nombre
FROM empleados
WHERE estado = 'Activo';



/*====================================================================*/
-- 24. UPDATE
-- El comando UPDATE en SQL se utiliza para modificar los datos existentes en una tabla.
-- SINTAXIS
UPDATE nombre_tabla
SET columna1 = valor1, columna2 = valor2, ...
WHERE condición;
--EJEMPLO
UPDATE empleados
SET salario = 70000, puesto = 'Gerente'
WHERE id_empleado = 2;


/*====================================================================*/
-- 25. DROP DATABASE
-- El comando DROP DATABASE en SQL se utiliza para eliminar completamente una base de datos, incluyendo todas sus tablas, vistas
-- SINTAXIS
DROP DATABASE nombre_base_datos;
--EJEMPLO
DROP DATABASE MI_BASE


/*====================================================================*/
-- 26. DROP TABLE
-- El comando DROP TABLE en SQL se utiliza para eliminar completamente una tabla de la base de datos.
--SINTAXIS
DROP TABLE nombre_tabla
-- EJEMPLO
DROP TABLE DIM_CLIENTE;


/*====================================================================*/
-- 27. ALTER TABLE(MODIFY)
-- El comando ALTER TABLE (MODIFY), es utilizado para cambiar el tamaño de una columna
-- SINTAXIS
ALTER TABLE nombre_tabla
MODIFY nombre_columna VARCHAR2(nuevo_tamano);
-- EJEMPLO
ALTER TABLE DULCES_SYS
MODIFY NOMBRE VARCHAR2(30);


/*====================================================================*/
-- 28. ALTER TABLE(ADD)
-- El comando ALTER TABLE (ADD), es utilizado para agregar una nueva columna a la tabla
-- SINTAXIS
ALTER TABLE NOMBRE_TABLE ADD COLUMNA TIPO;

--EJEMPLO
ALTER TABLE DULCERIA ADD FECHA_INICIO DATE;


/*====================================================================*/
-- 29. ALTER TABLE(RENAME)
-- El comando ALTER TABLE (RENAME), es utilizado para cambiar el nombre de una columna
-- SINTAXIS
ALTER TABLE nombre_de_tabla RENAME COLUMN nombre_viejo TO nombre_nuevo;

--EJEMPLO
ALTER TABLE CLIENTE RENAME COLUMN NOMBRE TO PRIMER_NOMBRE;


/*====================================================================*/
-- 30. ALTER TABLE(DROP)
-- El comando ALTER TABLE (DROP), es utilizado para eliminar alguna cokumna de la tabla
-- SINTAXIS
ALTER TABLE nombre_tabla DROP COLUMN nombre_columna;

--EJEMPLO
ALTER TABLE CLIENTE DROP COLUMN TELEFONO2;