<?php include('../templates/header.html'); ?>

<body>
<?php
    require("../config/conexion.php");

    $tipo = $_POST["tipo_vehiculo"];
    $edad1 = $_POST["edad1"];
    $edad2 = $_POST["edad2"];

    $query = "SELECT Despachos.id, Despachos.fecha, Despachos.id_origen, Despachos.id_destino, Despachos.id_compra FROM Despachos, Vehiculos, RelacionVR, Personal WHERE Vehiculos.id = Despachos.id_vehiculo AND Vehiculos.id = RelacionVR.id_vehiculo AND RelacionVR.id_repatidor = Personal.id ;";

    $resultado = $bbdd -> prepare($query);
    $resultado -> execute();
    $consulta = $resultado -> fetchAll();
?>

<table>
    <tr>
        <th>ID Despacho</th>
        <th>Fecha Despacho</th>
        <th>ID Origen</th>
        <th>ID Destino</th>
        <th>ID Compra</th>
    </tr>

    <?php
        foreach ($consulta as $c) {
            echo "<tr><td>$c[0]</td><td>$c[1]</td><td>$c[2]</td><td>$c[3]</td><td>$c[4]</td></tr>";
        }
    ?>

</table>

</body>