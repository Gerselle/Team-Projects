<?php
if (!empty($_POST['username'])){
$username = $_POST['username'];
$password = $_POST['password'];
$hashedPassword = hash("sha512",$password);
$fileUsername = "";
$filePassword = "";
$fileFace = "";
$lines = file('userpass.txt', FILE_SKIP_EMPTY_LINES|FILE_IGNORE_NEW_LINES);
$num = 0;
$exit = false;
/**foreach($lines as $line){
    if($line == "@&"){
        $num = 0;
    }
    if($exit){
        
    }
    elseif($num == 0){
        $fileUsername = $line;
        echo $line;
    }elseif($num == 1){
        $filePassword = $line;
        echo $line;
    }elseif($num == 2){
        $fileFace = $line;
        echo $line;
    }
    if($username == $fileUsername && $hashedPassword == $filePassword){
         echo "logged in as ".$fileUsername;
         #$exit = false;
    }
    echo $num;
    $num += 1;
    
}**/
foreach($lines as $line){
    if($exit){

    }elseif($num==0){
        $fileUsername = $line;
        echo $line;
    }elseif($num==1){
        $filePassword = $line;
        echo $line;
    }elseif($num==3){
        $fileFace = $line;
        echo $line;
    }
    elseif($username == $fileUsername && $hashedPassword == $filePassword){
        echo "logged in as ".$fileUsername;
        $exit = true;
    }elseif ($line == "@& "){
        echo $line;
        $fileUsername = "";
        $filePassword = "";
        $fileFace = "";
        $num = 0;
        
    }
    echo $num;
    $num+=1;
}
}



?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link  href="css/main.css"  rel="stylesheet"    >
    <title>Login</title>
</head>
<body>
    <h3>Login</h3>
    <form action="" method="post">
        <label for="">Username:</label><br />
        <input type="text" name="username"  required placholder="Enter the First Name"> <br />
        <label for="">Password:</label><br />
        <input type="text" name="password"  required placholder="Enter the First Name"> <br />
        <input type="submit"/>
    </form>
    <form action = "index.php">
        <label for="">Don't have a Profile</label><br />
        <button>Create Profile</button>
    </form>
</body>
</html>