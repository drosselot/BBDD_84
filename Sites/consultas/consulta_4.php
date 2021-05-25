<?php include('../templates/header.html'); ?>

<body>
<?php
    require("../config/conexion.php");

    $tipo = $_POST["tipo_vehiculo"];
    $edad1 = $_POST["edad1"];
    $edad2 = $_POST["edad2"];

    $query = "SELECT Despachos.id, Despachos.fecha, Despachos.id_origen, Despachos.id_destino, Despachos.id_compra, Despachos.id_vehiculo, Despachos.id_repartidor, Personal.edad FROM Despachos, Vehiculos, RelacionVR, Personal WHERE Vehiculos.tipo = '$tipo' AND Personal.edad BETWEEN $edad1 AND $edad2 AND Vehiculos.id = Despachos.id_vehiculo AND Vehiculos.id = RelacionVR.id_vehiculo AND RelacionVR.id_repartidor = Personal.id ;";

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
        <th>ID Vehiculo</th>
        <th>ID Repartidor</th>
        <th>Edad Repartidor</th>
    </tr>

    <?php
        foreach ($consulta as $c) {
            echo "<tr><td>$c[0]</td><td>$c[1]</td><td>$c[2]</td><td>$c[3]</td><td>$c[4]</td><td>$c[5]</td><td>$c[6]</td><td>$c[7]</td></tr>";
        }
    ?>

</table>

</body>