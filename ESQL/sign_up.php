<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device=width, initial-scale=1.0">
    <title>My SHOP</title>
</head>

<body>
    <h2>My SHOP</h2>
    <h3>Sign UP</h3>
    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="page_order.html">Order/Cart</a></li>
        <li><a href="page_my_page.html">My Page</a></li>
        <li><a href="page_sign_up.html">Sign Up</a></li>
    </ul>
    <?php
        function format_phone_number($input) {
            // xxx-xxxx-xxxx 형식으로 전화번호를 세팅해주는 함수
            $phone_num = preg_replace('/[^0-9]/', '', $input);
            $first = substr($phone_num, 0, 3);
            $second = substr($phone_num, 7);
            $third = substr($phone_num, 7, 10);
            $result = $first."-".$second.'-'.$third;
        
            return $result;
        }
        
        $db = mysqli_connect("localhost", "root", "sks0hn01!!", "product-purchase-history-management");
        if (mysqli_connect_errno()) {
            echo "Error: Could not connect to database server.";
            exit;
        }
        $newID = $_POST['newID'];
        $newPW = $_POST['newPW'];
        $newNAME = $_POST['newNAME'];
        $newAGE = $_POST['newAGE'];
        $sex = $_POST['sex'];
        $newCITY = $_POST['newCITY'];
        $newPhoneNUM = $_POST['newPhoneNUM'];

        $sign_up = $db->query("SELECT * FROM customer WHERE CusID='$newID' AND CusPW='$newPW'");

        if ($newPhoneNUM != '') {
            
            $phone_num = format_phone_number($newPhoneNUM);
        }
        else {
            $newPhoneNUM = null;
        }

        if($sign_up->num_rows >= 1){
            echo "<h2><br>이미 존재하는 ID입니다.</h2>";
        }
        else {
            $insert = "INSERT INTO customer (CusID, CusPW, CusNAME, AGE, PhoneNUM, CITY, SEX) values ('$newID', '$newPW', '$newNAME', '$newAGE', '$phone_num', '$newCITY', '$sex')";
            $db->query($insert);

            echo "<h2><br>가입이 완료되었습니다.</h2>";
        }
        // http://localhost:88/sign_up.php
    ?>
</body>
</html>