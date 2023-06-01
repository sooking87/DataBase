<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device=width, initial-scale=1.0">
    <title>My SHOP</title>
</head>

<body>
    <h3>카트 내역 조회 결과</h3>

    <?php
        $db = mysqli_connect("localhost", "root", "sks0hn01!!", "product-purchase-history-management");
        if (mysqli_connect_errno()) {
            echo "Error: Could not connect to database server.";
            exit;
        }
        $userID = $_POST['userID'];
        $userPW = $_POST['userPW'];

    ?>
    <table border="1" id="order-table">
        <tr>
            <th>카테고리</th> <!--0-->
            <th>상품명</th> <!--1-->
            <th>가격</th> <!--2-->
            <th>넣은 날짜</th> <!--3-->
        </tr>
        <?php
            $db = mysqli_connect("localhost", "root", "sks0hn01!!", "product-purchase-history-management");
            if (mysqli_connect_errno()) {
                echo "Error: Could not connect to database server.";
                exit;
            }

            $sql = "SELECT PINFO, PNAME, PRICE, InDATE FROM product, customer, cart WHERE customer.CusID = cart.CusID AND product.PNO = cart.PNO AND customer.CusID='$userID' AND CusPW='$userPW'";
            $result = mysqli_query($db, $sql);
            while ($row = mysqli_fetch_row($result)) {
                echo "<tr>";
                echo "<td>$row[0]</td><td>$row[1]</td><td>$row[2]</td><td>$row[3]</td>";
                echo "<tr>";
            }
        ?>
    </table>
    
</body>
</html>