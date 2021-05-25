<?php include('../templates/header.html'); ?>

<body>
<?php
    require("../config/conexion.php");

    $comuna = $_POST["comuna"];

    $query = "SELECT Vehiculos.id, Vehiculos.patente FROM Vehiculos, Unidades, Direcciones, Comunas WHERE Vehiculos.id_unidad = Unidades.id AND Unidades.id_direccion = Direcciones.id AND Direcciones.id_comuna = Comunas.id AND Comunas.comuna LIKE '%$comuna%';";

    $resultado = $bbdd -> prepare($query);
    $resultado -> execute();
    $consulta2 = $resultado -> fetchAll();
?>

<table>
    <tr>
        <th>ID</th>
        <th>Patente</th>
    </tr>

    <?php
        foreach ($consulta2 as $c2) {
            echo "<tr><td>$c2[0]</td><td>$c2[1]</td></tr>";
        }
    ?>

</table>

</body>