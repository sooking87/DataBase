<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device=width, initial-scale=1.0">
    <title>My SHOP</title>
</head>

<body>
    <h3>주문이 완료되었습니다.</h3>

    <?php
        $db = mysqli_connect("localhost", "root", "sks0hn01!!", "product-purchase-history-management");
        if (mysqli_connect_errno()) {
            echo "Error: Could not connect to database server.";
            exit;
        }
        $category = $_POST['category'];
        $num = $_POST['num'];
        $PINFO = strtoupper($category);
        $num = (int)$num;

        $sql = 'SELECT * FROM(SELECT ROW_NUMBER() OVER(ORDER BY PRICE) AS num, PNO, PNAME, PRICE, CNT FROM product WHERE PINFO="$PINFO") temp WHERE temp.num="$num"';
        $result = mysqli_query($db, $sql);
        $row = mysqli_fetch_row($result);
        print_r($row);
        if ($row) {
            echo "<h2>tlqkf</h2>";
        }
    ?>
    
</body>
</html>