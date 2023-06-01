<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device=width, initial-scale=1.0">
    <title>My SHOP</title>
</head>

<body>
    <h2>My SHOP</h2>
    <h3>비밀번호 조회 결과</h3>

    <?php
        $db = mysqli_connect("localhost", "root", "sks0hn01!!", "product-purchase-history-management");
        if (mysqli_connect_errno()) {
            echo "Error: Could not connect to database server.";
            exit;
        }
        $userID = $_POST['userID'];

        $sign_in = $db->query("SELECT CusPW FROM customer WHERE CusID='$userID'");

        while ($row = mysqli_fetch_row($sign_in)) {
            echo "<div>$userID 님의 비밀번호 조회 결과 =>".$row[0]."</div>";
        }
        // http://localhost:88/sign_up.php
    ?>
</body>
</html>