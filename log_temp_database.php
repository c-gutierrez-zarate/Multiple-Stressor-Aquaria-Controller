<?php

include 'php/conexion.php';
$conexion = conexion();

$name = $_GET["name"];
$T1 = $_GET["T1"];
$T2 = $_GET["T2"];
$T3 = $_GET["T3"];
$T4 = $_GET["T4"];
$T5 = $_GET["T5"];
$T6 = $_GET["T6"];
$T7 = $_GET["T7"];
$T8 = $_GET["T8"];
$BM1tank=$_GET["BM1tank"];
$BM1blanco = $_GET["BM1blanco"];
$BM1negro = $_GET["BM1negro"];
$BM2tank = $_GET["BM2tank"];
$BM2rojo = $_GET["BM2rojo"];
$BM2azul = $_GET["BM2azul"];
$BM3tank = $_GET["BM3tank"];
$BM3blanco = $_GET["BM3blanco"];
$BM3negro = $_GET["BM3negro"];
$BM4tank = $_GET["BM4tank"];
$BM4rojo = $_GET["BM4rojo"];
$BM4azul = $_GET["BM4azul"];
$Tsala = $_GET["Tsala"];
$Tagua = $_GET["Tagua"];
$Tcap = $_GET["Tcap"];


if (($T1!="") and ($T2!="") and ($T3!="") and ($T4!="") and ($T5!="") and ($T6!="") and ($T7!="") and ($T8!="") and ($BM1tank!="") and ($BM1blanco!="") and ($BM1negro!="") and ($BM2tank!="") and ($BM2rojo!="") and ($BM2azul!="") and ($BM3tank!="") and ($BM3blanco!="") and ($BM3negro!="") and ($BM4tank!="") and ($BM4rojo!="") and ($BM4azul!="") and ($Tsala!="") and ($Tagua!="")) {
    
    $sql = "insert data_temp (date, name, temp_T1, temp_T2, temp_T3, temp_T4,temp_T5, temp_T6, temp_T7, temp_T8, temp_BM1, temp_BM1_blanco, temp_BM1_negro, temp_BM2, temp_BM2_rojo, temp_BM2_azul, temp_BM3, temp_BM3_blanco, temp_BM3_negro, temp_BM4, temp_BM4_rojo, temp_BM4_azul, temp_Sala, temp_Agua, temp_Cap) values (NOW(),'$name','$T1','$T2','$T3','$T4','$T5','$T6','$T7','$T8','$BM1tank','$BM1blanco','$BM1negro','$BM2tank','$BM2rojo','$BM2azul','$BM3tank','$BM3blanco','$BM3negro','$BM4tank','$BM4rojo','$BM4azul','$Tsala','$Tagua','$Tcap')";
    mysqli_query($conexion,$sql);
        echo ' ok, all temperature data have been saved';
}else{
    
        echo 'data from some probes is missing <br>';
echo "T1=$T1<br>";
echo "T2=$T2<br>";
echo "T3=$T3<br>";
echo "T4=$T4<br>";
echo "T5=$T5<br>";
echo "T6=$T6<br>";
echo "T7=$T7<br>";
echo "T8=$T8<br>";
echo "BM1tank=$BM1tank<br>";
echo "BM1blanco=$BM1blanco<br>";
echo "BM1negro=$BM1negro<br>";
echo "BM2tank=$BM2tank<br>";
echo "BM2rojo=$BM2rojo<br>";
echo "BM2azul=$BM2azul<br>";
echo "BM3tank=$BM3tank<br>";
echo "BM3blanco=$BM3blanco<br>";
echo "BM3negro=$BM3negro<br>";
echo "BM4tank=$BM4tank<br>";
echo "BM4rojo=$BM4rojo<br>";
echo "BM4azul=$BM4azul<br>";
echo "Tsala=$Tsala<br>";
echo "Tagua=$Tagua<br>";
echo "Tcap=$Tcap<br>";
}
?>
