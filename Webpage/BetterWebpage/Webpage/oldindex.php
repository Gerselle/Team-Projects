<?php
if (!empty($_POST['username'])){
$username = $_POST['username'];
$password = $_POST['password'];
$hashedPassword = hash("sha512",$password);
echo $hashedPassword;


$myfile = fopen('userpass.txt', 'a') or die("Unable to open file!");
$text = $username."\n".$hashedPassword."\n"."@& \n";
fwrite($myfile, $text);
fclose($myfile);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link  href="css/main.css"  rel="stylesheet"    >
    <title>Profile Creation</title>
</head>
<body>
    <h3>Create Your Profile</h3>
    <form action="picture.php" method="post">
        <label for="">Username:</label><br />
        <input type="text" name="username"  required placholder="Enter the First Name"> <br />
        <label for="">Password:</label><br />
        <input type="text" name="password"  required placholder="Enter the First Name"> <br />
        <input type="submit"/>
    </form>
    
    <!--<form action="display.php">
        <input type="submit" value="See text file"/>
    </form>-->
    <form action = "login.php">
        <label for="">Want to access game past game data:</label><br />
    <button>
        login
    </button>
    </form>

</body>
</html>