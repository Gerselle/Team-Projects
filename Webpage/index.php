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
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/webcamjs/1.0.25/webcam.min.js"></script>
    <link  href="css/main.css"  rel="stylesheet"    >
    <title>Profile Creation</title>
</head>
<body>
    <h3>Create Your Profile</h3>
    <form action="store.php" method="post">
    
        <label for="">Username:</label><br />
        <input type="text" name="username"  required placholder="Enter the First Name"> <br />
        <label for="">Password:</label><br />
        <input type="text" name="password"  required placholder="Enter the First Name"> <br />
        <div class="row">
            <div class="col-md-6">
                <div id="my_camera"></div>
                <br/>
                <input type=button value="Take Picture" onClick="facePicture()">
                <input type="hidden" name="face" class="image-tag">
            </div>
            <div class="col-md-6">
                <div id="results">If on Mobile Device press "Take Picture" twice</div>
            </div>
        </div>
        <div></div>
        <input type="submit"/>
        <div></div>
    </form>
    
    <!--<form action="display.php">
        <input type="submit" value="See text file"/>
    </form>-->

    <form action = "login.php">
        <label for="">Already have an account:</label><br />
    <button>
        Game Lobby
    </button>
    </form>

    <script language="JavaScript">
    Webcam.set({
        width: 490,
        height: 390,
        image_format: 'jpeg',
        jpeg_quality: 90
    });
  
    Webcam.attach( '#my_camera' );
  
    function facePicture() {
        Webcam.snap( function(data_uri) {
            $(".image-tag").val(data_uri);
            document.getElementById('results').innerHTML = '<img src="'+data_uri+'"/>';
        } );
    }
</script>

</body>
</html>