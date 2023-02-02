<?php
$host = 'localhost';
$user = 'root';
$pass = '';
$dName = 'cromwell';
$sql = "CREATE DATABASE IF NOT EXISTS cromwell";
$link = mysqli_connect($host,$user,$pass);
mysqli_query($link,$sql);
$conn = mysqli_connect($host,$user,$pass,$dName);

?>