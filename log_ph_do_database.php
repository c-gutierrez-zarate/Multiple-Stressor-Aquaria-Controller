
<?php

include 'php/conexion.php'; 
$conexion = conexion(); 

$name = $_GET["name"];
$temp_T1 = $_GET["temp_T1"];
$temp_T2 = $_GET["temp_T2"];
$temp_T3 = $_GET["temp_T3"];
$temp_T4 = $_GET["temp_T4"];
$temp_T5 = $_GET["temp_T5"];
$temp_T6 = $_GET["temp_T6"];
$temp_T7 = $_GET["temp_T7"];
$temp_T8 = $_GET["temp_T8"];
$temp_C1 = $_GET["temp_T9"];
$temp_C2 = $_GET["temp_T10"];
$ph_T1 = $_GET["ph_T1"];
$ph_T2 = $_GET["ph_T2"];
$ph_T3 = $_GET["ph_T3"];
$ph_T4 = $_GET["ph_T4"];
$ph_T5 = $_GET["ph_T5"];
$ph_T6 = $_GET["ph_T6"];
$ph_T7 = $_GET["ph_T7"];
$ph_T8 = $_GET["ph_T8"];
$ph_C1 = $_GET["ph_T9"];
$ph_C2 = $_GET["ph_T10"];
$od_T1 = $_GET["od_T1"];
$od_T2 = $_GET["od_T2"];
$od_T3 = $_GET["od_T3"];
$od_T4 = $_GET["od_T4"];
$od_T5 = $_GET["od_T5"];
$od_T6 = $_GET["od_T6"];
$od_T7 = $_GET["od_T7"];
$od_T8 = $_GET["od_T8"];
$od_C1 = $_GET["od_T9"];
$od_C2 = $_GET["od_T10"];
$od_T1mg = $_GET["od_T1mg"];
$od_T2mg = $_GET["od_T2mg"];
$od_T3mg = $_GET["od_T3mg"];
$od_T4mg = $_GET["od_T4mg"];
$od_T5mg = $_GET["od_T5mg"];
$od_T6mg = $_GET["od_T6mg"];
$od_T7mg = $_GET["od_T7mg"];
$od_T8mg = $_GET["od_T8mg"];
$od_C1mg = $_GET["od_T9mg"];
$od_C2mg = $_GET["od_T10mg"];


if (($temp_T1 != "") and ($temp_T2 != "") and ($temp_T3 != "") and ($temp_T4 != "") and ($temp_T5 != "") and ($temp_T6 != "") and ($temp_T7 != "") and ($temp_T8 != "") and ($temp_C1 != "") and ($temp_C2 != "")) {

    $sql_temp = "insert data_temp_ph_od (date, name, temp_T1, temp_T2, temp_T3, temp_T4, temp_T5, temp_T6, temp_T7, temp_T8, temp_C1, temp_C2) values (NOW(),'$name','$temp_T1','$temp_T2','$temp_T3','$temp_T4','$temp_T5','$temp_T6','$temp_T7','$temp_T8','$temp_C1','$temp_C2')";
    mysqli_query($conexion, $sql_temp);

    
    echo ' ok, all temperature data have been saved';
} else {
    echo 'data from some probes is missing <br>';
    echo "T1=$temp_T1<br>";
    echo "T2=$temp_T2<br>";
    echo "T3=$temp_T3<br>";
    echo "T4=$temp_T4<br>";
    echo "T5=$temp_T5<br>";
    echo "T6=$temp_T6<br>";
    echo "T7=$temp_T7<br>";
    echo "T8=$temp_T8<br>";
    echo "T9=$temp_C1<br>";
    echo "T9=$temp_C2<br>";
}

if (($ph_T1 != "") and ($ph_T2 != "") and ($ph_T3 != "") and ($ph_T4 != "") and ($ph_T5 != "") and ($ph_T6 != "") and ($ph_T7 != "") and ($ph_T8 != "") and ($ph_C1 != "") and ($ph_C2 != "")) {

    $sql_ph = "insert data_ph (date, name, ph_T1, ph_T2, ph_T3, ph_T4, ph_T5, ph_T6, ph_T7, ph_T8, ph_C1, ph_C2) values (NOW(),'$name','$ph_T1','$ph_T2','$ph_T3','$ph_T4','$ph_T5','$ph_T6','$ph_T7','$ph_T8','$ph_C1','$ph_C2')";
    mysqli_query($conexion, $sql_ph);

    echo ' ok, all pH data have been saved';
} else {
    echo 'faltan data de alguna sonda <br>';
    echo "Ph1=$ph_T1<br>";
    echo "Ph2=$ph_T2<br>";
    echo "Ph3=$ph_T3<br>";
    echo "Ph4=$ph_T4<br>";
    echo "Ph5=$ph_T5<br>";
    echo "Ph6=$ph_T6<br>";
    echo "Ph7=$ph_T7<br>";
    echo "Ph8=$ph_T8<br>";
    echo "Ph9=$ph_C1<br>";
    echo "Ph10=$ph_C2<br>";
}

if (($od_T1 != "") and ($od_T2 != "") and ($od_T3 != "") and ($od_T4 != "") and ($od_T5 != "") and ($od_T6 != "") and ($od_T7 != "") and ($od_T8 != "") and ($od_C1 != "") and ($od_C2 != "")) {

    $sql_od = "insert data_od (date, name, od_T1, od_T2, od_T3, od_T4, od_T5, od_T6, od_T7, od_T8, od_C1, od_C2) values (NOW(),'$name','$od_T1','$od_T2','$od_T3','$od_T4','$od_T5','$od_T6','$od_T7','$od_T8','$od_C1','$od_C2')";
    mysqli_query($conexion, $sql_od);

       echo ' ok, all DO (%sat) data have been saved';
} else {
    echo 'data from some probes is missing <br>';
    echo "Od1=$od_T1<br>";
    echo "Od2=$od_T2<br>";
    echo "Od3=$od_T3<br>";
    echo "Od4=$od_T4<br>";
    echo "Od5=$od_T5<br>";
    echo "Od6=$od_T6<br>";
    echo "Od7=$od_T7<br>";
    echo "Od8=$od_T8<br>";
    echo "Od9=$od_C1<br>";
    echo "Od10=$od_C2<br>";
}

if (($od_T1mg != "") and ($od_T2mg != "") and ($od_T3mg != "") and ($od_T4mg != "") and ($od_T5mg != "") and ($od_T6mg != "") and ($od_T7mg != "") and ($od_T8mg != "") and ($od_C1mg != "") and ($od_C2mg != "")) {

    $sql_od_mg = "insert data_od_mgl (date, name, od_T1_mg, od_T2_mg, od_T3_mg, od_T4_mg, od_T5_mg, od_T6_mg, od_T7_mg, od_T8_mg, od_C1_mg, od_C2_mg) values (NOW(),'$name','$od_T1mg','$od_T2mg','$od_T3mg','$od_T4mg','$od_T5mg','$od_T6mg','$od_T7mg','$od_T8mg','$od_C1mg','$od_C2mg')";
    mysqli_query($conexion, $sql_od_mg);

       echo ' ok, all DO (mg/L) data have been saved';
} else {
    echo 'data from some probes is missing <br>';
    echo "Od1mg=$od_T1mg<br>";
    echo "Od2mg=$od_T2mg<br>";
    echo "Od3mg=$od_T3mg<br>";
    echo "Od4mg=$od_T4mg<br>";
    echo "Od5mg=$od_T5mg<br>";
    echo "Od6mg=$od_T6mg<br>";
    echo "Od7mg=$od_T7mg<br>";
    echo "Od8mg=$od_T8mg<br>";
    echo "Od9mg=$od_C1mg<br>";
    echo "Od10mg=$od_C2mg<br>";
}
?>

