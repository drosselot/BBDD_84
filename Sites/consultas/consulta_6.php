<?php include('../templates/header.html'); ?>

<body>
<?php
    require("../config/conexion.php");

    $tipo = $_POST["tipo_vehiculo"];

    $query = "SELECT Unidades.id, Count(Vehiculos.id) as N_Vehiculos FROM Vehiculos, Unidades WHERE Vehiculos.id_unidad = Unidades.id AND Vehiculos.tipo LIKE '%$tipo%' GROUP BY Unidades.id;";

    $resultado = $bbdd -> prepare($query);
    $resultado -> execute();
    $consulta2 = $resultado -> fetchAll();
?>

<table>
    <tr>
        <th>ID</th>
        <th>Numero Vehiculos</th>
    </tr>

    <?php
        echo "<tr><td>$consulta2[0]</td><td>$consulta2[1]</td></tr>";
    ?>

</table>

</body>
