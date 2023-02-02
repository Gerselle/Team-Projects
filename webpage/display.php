<?php  
include'conn.php';
 ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link  href="css/main.css"  rel="stylesheet"    >
    <title>Player Information</title>
</head>
<body>
    <h2>Player Information</h2>
    <?php 
        $select ="SELECT * FROM player_tbl;";
        $result = mysqli_query($conn, $select);
        $check = mysqli_num_rows($result); 
    ?>
    <table>
        <tr>
            <th>Id Number</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Image</th>
            <th>Face</th>
        </tr>
    <?php
       if($check > 0)
       {
            while($row = mysqli_fetch_array( $result) )
            {
                echo"<tr>";
                    echo "<td>" . $row['playerId']   .   "</td>";
                    echo "<td>" . $row['firstName']    .   "</td>";
                    echo "<td>" . $row['lastName']   .   "</td>";
                    echo "<td>" . $row['email']   .   "</td>";
                    echo "<td> <img src='images/" . $row['images']   ."'width='75'" . "height='75'" .   "'/></td>";
                    echo "<td>" . $row['face']   .   "</td>";
                echo"</tr>";
            }

       }
    ?>
    </table>
    <form action="index.php">
        <input type="submit" value="Go to Home"/>
    </form>
</body>
</html>