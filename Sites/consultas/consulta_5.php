<?php include('../templates/header.html'); ?>

<body>
<?php
    require("../config/conexion.php");

    $comuna1 = $_POST["comuna1"];
    $comuna1 = strtolower("$comuna1");
    $comuna2 = $_POST["comuna2"];
    $comuna2 = strtolower("$comuna2");

    $query = "SELECT Unidades.id, Personal.id, Personal.nombre, Personal.rut, Personal.sexo, Personal.edad FROM Personal, Unidades, Cobertura, Comunas WHERE Cobertura.id_comuna = Comunas.id AND Personal.id = Unidades.id_jefe AND Unidades.id = Cobertura.id_unidad AND Comunas.comuna LIKE '%$comuna2%' AND Unidades.id IN (SELECT Unidades.id FROM Unidades, Cobertura, Comunas WHERE Unidades.id = Cobertura.id_unidad AND Comunas.id = Cobertura.id_comuna AND Comunas.comuna LIKE '%$comuna1%' GROUP BY Unidades.id) GROUP BY (Unidades.id, Personal.id, Personal.nombre, Personal.rut, Personal.sexo, Personal.edad);";

    $resultado = $bbdd -> prepare($query);
    $resultado -> execute();
    $consulta2 = $resultado -> fetchAll();
?>

<table align="center" cellspacing="2" cellpadding="2" border="1">
    <tr>
        <th>ID Unidad</th>
        <th>ID Jefe</th>
        <th>Nombre</th>
        <th>RUT</th>
        <th>Sexo</th>
        <th>Edad</th>
    </tr>

    <?php
        foreach ($consulta2 as $c2) {
            echo "<tr><td>$c2[0]</td><td>$c2[1]</td><td>$c2[2]</td><td>$c2[3]</td><td>$c2[4]</td><td>$c2[5]</td></tr>";
        }
    ?>

</table>

</body>