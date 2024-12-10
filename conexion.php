<?php
function conexion() {
    // Database connection parameters
    $host = 'localhost',
    $user = 'XXXX', #add info
    $password = 'XXXX', #add info
    $database = 'XXXX', #add database name

    // Create a connection
    $conexion = new mysqli($host, $user, $password, $database);

    // Check connection
    if ($conexion->connect_error) {
        die("Connection failed: " . $conexion->connect_error);
    }

    // Optionally set the charset to utf8
    $conexion->set_charset("utf8");

    return $conexion;
}
?>