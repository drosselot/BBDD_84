<?php include('../templates/header.html'); ?>

<body>
<?php
    require("../config/conexion.php");

    $tipo = $_POST["tipo_vehiculo"];

    $query = "SELECT Cantidades.id, Cantidades.cantidad, Maximo.mayor FROM (SELECT Unidades.id, COUNT(Vehiculos.id) as cantidad FROM Unidades, Vehiculos WHERE Vehiculos.id_unidad = Unidades.id AND Vehiculos.tipo LIKE '%$tipo%' GROUP BY Unidades.id) as Cantidades, (SELECT MAX(cantidad2) as mayor FROM (SELECT Unidades.id, COUNT(Vehiculos.id) as cantidad2 FROM Unidades, Vehiculos WHERE Vehiculos.id_unidad = Unidades.id AND Vehiculos.tipo LIKE '%$tipo%' GROUP BY Unidades.id ORDER BY Unidades.id) as Tabla1) as Maximo WHERE Cantidades.cantidad = Maximo.mayor;";

    $resultado = $bbdd -> prepare($query);
    $resultado -> execute();
    $consulta2 = $resultado -> fetchAll();
?>

<table>
    <tr>
        <th>ID Unidad</th>
        <th>Numero Vehiculos</th>
    </tr>

    <?php
        echo "<tr><td>$consulta2[0]</td><td>$consulta2[1]</td></tr>";
    ?>

</table>

</body>


SELECT Cantidades.id, Cantidades.cantidad, Maximo.mayor FROM (SELECT Unidades.id, COUNT(Vehiculos.id) as cantidad FROM Unidades, Vehiculos WHERE Vehiculos.id_unidad = Unidades.id AND Vehiculos.tipo LIKE '%$tipo%' GROUP BY Unidades.id) as Cantidades, (SELECT MAX(cantidad2) as mayor FROM (SELECT Unidades.id, COUNT(Vehiculos.id) as cantidad2 FROM Unidades, Vehiculos WHERE Vehiculos.id_unidad = Unidades.id AND Vehiculos.tipo LIKE '%$tipo%' GROUP BY Unidades.id ORDER BY Unidades.id) as Tabla1) as Maximo WHERE Cantidades.cantidad = Maximo.mayor;