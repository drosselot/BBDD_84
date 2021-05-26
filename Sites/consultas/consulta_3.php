<?php include('../templates/header.html'); ?>

<body>
<?php
    require("../config/conexion.php");

    $comuna = $_POST["comuna"];
    $ano = $_POST["ano"]; 

    $query = "SELECT Vehiculos.id, Vehiculos.patente, Vehiculos.estado, Vehiculos.tipo FROM Vehiculos, Despachos, Direcciones, Comunas WHERE DATE_PART('year', Despachos.fecha) = $ano AND Vehiculos.id = Despachos.id_vehiculo AND Despachos.id_destino = Direcciones.id AND Direcciones.id_comuna = Comunas.id AND Comunas.comuna LIKE '%$comuna%';";

    $resultado = $bbdd -> prepare($query);
    $resultado -> execute();
    $consulta2 = $resultado -> fetchAll();
?>

<table>
    <tr>
        <th>ID</th>
        <th>Patente</th>
        <th>Estado</th>
        <th>Tipo</th>
    </tr>

    <?php
        foreach ($consulta2 as $c2) {
            echo "<tr><td>$c2[0]</td><td>$c2[1]</td><td>$c2[2]</td><td>$c2[3]</td></tr>";
        }
    ?>

</table>

</body>