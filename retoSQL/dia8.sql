Consulta del día #8: Práctica
Tarea:

1. Encuentra los empleados que hayan cumplido más de 5 años en la empresa.
2. Calcula cuántos días faltan para el próximo aniversario laboral de cada empleado.
3. Muestra su nombre, fecha de ingreso, años en la empresa, y días hasta el próximo aniversario.


SELECT NOMBRE_EMPLEADO, FECHA_INGRESO, MONTHS_BETWEEN(SYSDATE, FECHA_INGRESO) AS ANTIGUEDAD
FROM EMPLEADOS
WHERE FECHA_INGFRESO > MONTHS_BETWEEN(SYSDATE, FECHA_INGRESO);

--Corrección
SELECT NOMBRE_EMPLEADO, 
        FECHA_INGRESO, 
        FLOOR(MONTHS_BETWEEN(SYSDATE, FECHA_INGRESO) / 12) AS ANTIGUEDAD_ANIOS,
        TRUNC(ADD_MONTHS(FECHA_INGRESO, (FLOOR(MONTHS_BETWEEN(SYSDATE, FECHA_INGRESO) / 12) + 1) * 12) - SYSDATE) AS DIAS_PARA_ANIVERSARIO
FROM EMPLEADOS
WHERE FLOOR(MONTHS_BETWEEN(SYSDATE, FECHA_INGRESO) / 12) >= 5
ORDER BY DIAS_PARA_ANIVERSARIO ASC;
