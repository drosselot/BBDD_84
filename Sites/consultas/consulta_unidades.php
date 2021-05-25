<?php include('../templates/header.html'); ?>

<body>
<?php
    require("../config/conexion.php");

    $query = "SELECT Unidades.id, Direcciones.nombre, Comunas.comuna FROM Unidades, Direcciones, Comunas WHERE Unidades.id_direccion = Direcciones.id AND Direcciones.id_comuna = Comunas.id;";

    $resultado = $bbdd -> prepare($query);
    $resultado -> execute();
    $unidades = $resultado -> fetchAll();
?>

<table>
    <tr>
        <th>id</th>
        <th>direccion</th>
        <th>comuna</th>
    </tr>

    <?php
        foreach ($unidades as $unidad) {
            echo "<tr><td>$unidad[0]</td><td>$unidad[1]</td><td>$unidad[2]</td></tr>";
        }
    ?>

</table>

</body>
</html>