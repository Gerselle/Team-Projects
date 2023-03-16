<?php
$username = $_POST['username'];
$password = $_POST['password'];
$email = $_POST['email'];
$face = $_POST['face'];

$myfile = fopen('userpass.txt', 'w') or die("Unable to open file!");
$text = $username; #+ "\n" + $password + "\n" + $email + "\n" + $face + "\n";
fwrite($myfile, $text);
fclose($myfile);
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
    <form action="" method="post">
        <label for="">Username:</label><br />
        <input type="text" name="username"  required placholder="Enter the First Name"> <br />
        <label for="">Password:</label><br />
        <input type="text" name="password"  required placholder="Enter the First Name"> <br />
        <label for="">Email:</label><br />
        <input type="text" name="email"  required placholder="Enter the email"> <br /> 
        <div>
        <label for="">Do you want your face scanned and added to your profile?</label><br />
        <input type="checkbox" name="face" id="" value="yes">
        </div>
        <input type="submit"/>
    </form>
    <form action="display.php">
        <input type="submit" value="See text file"/>
    </form>
</body>
</html>