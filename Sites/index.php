<?php include('templates/header.html'); ?>

<body>
    <h1 align="center"> Mi Tienda Web </h1>

    <br>

    <h2 align="center"> Buscar datos de empresas: </h2>

    <!-Consulta 1 ###########################->

    <h3> Obtener todas las unidades de la empresa de despacho: </h3>
    <br>
    <form action="consultas/consulta_unidades.php" method="post">
        <input type="submit" value="Buscar">
    </form>

    <br>

    <!-Consulta 2 ###########################->

    <h3> Vehiculos de la unidades ubicadas en la comuna de: </h3>
    <br>
    <form action="consultas/consulta_2.php" method="post">
        Ingrese una comuna:
        <input type="text" name="comuna">
        <br>
        <input type="submit" value="Buscar">
    </form>
    
    <br>

    <!-Consulta 3 ###########################->

    <h3> Vehiculos que realizaron despachos en la comuna y año seleccionados: </h3>
    <br>
    
    <?php
    #Primero obtenemos todas las fechas
    require("config/conexion.php");
    $result3 = $bbdd -> prepare("SELECT fecha FROM Despachos ORDER BY fecha;");
    $result3 -> execute();
    $dataCollected3 = $result3 -> fetchAll();

    ?>

    <form action="consultas/consulta_3.php" method="post">
        Comuna:
        <input type="text" name="comuna">
        <br>
        Año:
        <select name="ano">
            <?php
                foreach($dataCollected3 as $fechas) {
                echo "<option value=date($fechas[0] $Y)>date($fechas[0] $Y)</option>";
                }
            ?>
        </select>
        <br>
        <input type="submit" value="Buscar">
    </form>

    <br>

    <!-Consulta 4 ###########################->

    <h3> Despachos realizados por el tipo de vehiculo seleccionado, cuya edad del repaatidor esta en el rango seleccionado: </h3>
    <br>
    
    <?php
    #Primero obtenemos todas las fechas
    require("config/conexion.php");
    $result4 = $bbdd -> prepare("SELECT DISTINCT edad FROM Personal ORDER BY edad;");
    $result4 -> execute();
    $dataCollected4 = $result4 -> fetchAll();
    ?>

    <form action="consultas/consulta_4.php" method="post">
        Tipo de vehiculo:
        <input type="text" name="tipo_vehiculo">
        <br>
        Primera edad seleccionada:
        <select name="edad1">
            <?php
            foreach ($dataCollected4 as $d4) {
                echo "<option value=$d4[0]>$d4[0]</option>";
            }
            ?>
        </select>
        <br>
        Segunda edad seleccionada:
        <select name="edad2">
            <?php
            foreach ($dataCollected4 as $d4) {
                echo "<option value=$d4[0]>$d4[0]</option>";
            }
            ?>
        </select>
        <br>
        <input type="submit" value="Buscar">
    </form>

    <br>

    <!-Consulta 5 ###########################->

    <h3> Jefes que despachan a ambas comunas:</h3>
    <br>
    <form action="consultas/consulta_5.php" method="post">
        Comuna 1:
        <input type="text" name="comuna1">
        <br>
        Comuna 2:
        <input type="text" name="comuna2">
        <br>
        <input type="submit" value="Buscar">
    </form>

    <br>

    <!-Consulta 6 ########################### ->

    <h3> Unidad que mas maneja vehiculos de ese tipo de vehiculo: </h3>
    <br>
    <form action="consultas/consulta_6.php" method="post">
        Tipo de vehiculo:
        <input type="text" name="tipo_vehiculo">
        <br>
        <input type="submit" value="Buscar">
    </form>
    
</body>
</html>