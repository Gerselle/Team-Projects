<?php
if (!empty($_POST['username'])){
$username = $_POST['username'];
$password = $_POST['password'];
$hashedPassword = hash("sha512",$password);

$lines = file('userpass.txt');
$num = count(file('userpass.txt'));
$count = 0;
$loggedUser = true;
$loggedPass = true;

foreach($lines as $line) {
    $count++;
    if ($count % 3 == 1){
        if($line == $username . "\n"){
            $loggedUser = true;
        }else{
            $loggedUser = false;
        }
    }elseif($count % 3 == 2){
        if($line == $hashedPassword . "\n"){
            $loggedPass = true;
        }else{
            $loggedPass = false;
        }
    }
    
    if($loggedUser && $loggedPass && $count > 1){
     echo "Logged in";
    #$command = "python3 -c 'import test; test.greet()'";
    #$output = shell_exec($command);
    #echo $output;
    header("Location: game.php");       
    break;
    }elseif((($loggedUser || $loggedPass) || !($loggedUser && $loggedPass)) && $count >= $num){
        echo "Incorrect Username/Password";
    }
    #echo $line . "\n";
  
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
    <title>Account Login</title>
</head>
<body>
    <h3>Login</h3>
    <form action="" method="post">
    
        <label for="">Username:</label><br />
        <input type="text" name="username"  required placholder="Enter the First Name"> <br />
        <label for="">Password:</label><br />
        <input type="text" name="password"  required placholder="Enter the First Name"> <br />
        <div></div>
        <input type="submit"/>
        <div></div>
    </form>
</body>
</head>
</html>