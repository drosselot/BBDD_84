<?php include('../templates/header.html'); ?>

<body>
<?php
    require("../config/conexion.php");

    $comuna1 = $_POST["comuna1"];
    $comuna2 = $_POST["comuna2"];

    $query = "SELECT Pesonal.id, Personal.nombre FROM Personal, Unidades, Direcciones, Comunas WHERE Personal.id = Unidades.id_jefe AND Unidades.id_direccion = Direcciones.id AND Direcciones.id_comuna = Comunas.id AND Comunas.comuna LIKE '%$comuna1%' Comunas.comuna LIKE '%$comuna2%';";

    $resultado = $bbdd -> prepare($query);
    $resultado -> execute();
    $consulta2 = $resultado -> fetchAll();
?>

<table>
    <tr>
        <th>ID</th>
        <th>Jefe</th>
    </tr>

    <?php
        foreach ($consulta2 as $c2) {
            echo "<tr><td>$c2[0]</td><td>$c2[1]</td></tr>";
        }
    ?>

</table>

</body>