<?php 

include 'conn.php';


/*if(mysqli_query($link,$sql)){
    echo "it worked";
}else{
    echo "it didn't";
}*/

$myTable = 'CREATE TABLE IF NOT EXISTS player_tbl (
    playerId INT(5) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    email VARCHAR(25) NOT NULL,
    images longblob NOT NULL,
    face VARCHAR(25) NOT NULL
    )';
mysqli_query($conn, $myTable);

if(isset($_POST['submit'])){
    $firstName = $_POST['firstName'];
    $lastName = $_POST['lastName'];
    $email = $_POST['email'];
    $imageName =  $_FILES['upload']['name'];
    $tempName  =  $_FILES['upload']['tmp_name'];
    $fName = 'images/';
    $face = $_POST['face'];
    
    move_uploaded_file($tempName, $fName.$imageName);
    $insertTable = "INSERT INTO `player_tbl`(`firstName`,`lastName`,`email`, `images`,`face`)
            VALUES('$firstName', '$lastName','$email', '$imageName', '$face');";
    $run = mysqli_query($conn,$insertTable);
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
    <form action="" method="post" enctype="multipart/form-data">
        <label for="">First Name:</label><br />
        <input type="text" name="firstName"  required placholder="Enter the First Name"> <br />
        <label for="">Last Name:</label><br />
        <input type="text" name="lastName"  required placholder="Enter the Last Name"> <br />
        <label for="">Email:</label><br />
        <input type="text" name="email"  required placholder="Enter the email"> <br /> 
        <div> 
        <label for="">Image:<br />
        <input type="file" name="upload" id=""></label><br />
        </div>
        <div>
        <label for="">Do you want your face scanned and added to your profile?</label><br ?>
        <input type="checkbox" name="face" id="" value="yes">
        </div>
        <div>
        <button name="submit">Create Profile</button>
        </div>
    </form>
    <form action="display.php">
        <input type="submit" value="Create Profile"/>
    </form>
</body>
</html>