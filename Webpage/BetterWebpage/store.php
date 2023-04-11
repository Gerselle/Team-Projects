<?php
    $username = $_POST['username'];
    $password = $_POST['password'];
    $hashedPassword = hash("sha512",$password);
    $img = $_POST['face'];
    $folderPath = "images/";
  
    $image_parts = explode(";base64,", $img);
    $image_type_aux = explode("images/", $image_parts[0]);
    #$image_type = $image_type_aux[1];
  
    $image_base64 = base64_decode($image_parts[1]);
    $fileName =  $username .$hashedPassword. '.png';
  
    $file = $folderPath . $fileName;
    file_put_contents($file, $image_base64);
  
    print_r($fileName);

    $myfile = fopen('userpass.txt', 'a') or die("Unable to open file!");
    $text = $username."\n".$hashedPassword."\n"."@& \n";
    fwrite($myfile, $text);
    fclose($myfile);
  
?>