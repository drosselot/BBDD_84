<?php 
    try { 
        require('datos.php');
        $bbdd = new PDO("pgsql:dbname=$base;host=localhost;port=5432;user=$usuario;password=$contraseña");
    } catch (Exception $e) {
        echo "Error con conexion :( $e ";
    }
?>