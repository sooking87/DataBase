
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device=width, initial-scale=1.0">
    <title>My SHOP</title>
</head>

<body>
    <h2>My SHOP</h2>
    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="page_order.html">Order/Cart</a></li>
        <li><a href="page_my_page.html">My Page</a></li>
        <li><a href="page_sign_up.html">Sign Up</a></li>
    </ul>
    <?php
        $db = mysqli_connect("localhost", "root", "sks0hn01!!", "product-purchase-history-management");
        if (mysqli_connect_errno()) {
            echo "Error: Could not connect to database server.";
            exit;
        }
        $userID = $_POST['userID'];
        $userPW = $_POST['userPW'];
        

        $sign_in = $db->query("DELETE FROM customer WHERE CusID='$userID' AND CusPW='$userPW'");

        echo "<h3>탈퇴가 완료되었습니다.</h3>";
    ?>
</body>

</html>