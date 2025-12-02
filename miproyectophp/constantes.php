<?php
    #VERSION VIEJA
    echo("Constantes en php");

    define("NOMBRE", "Sebastian");

    define("NOMBRE", 9);

    echo NOMBRE;

    #VERSION NUEVA
    const NOMBRE2 = "PEDRO";

    const NOMBRE2 = "pedro";

    echo NOMBRE2;

    #definir arrays constantes
    define("ALUMNOS", array("juan", "pedro", "sofia"));
    echo ALUMNOS[1];