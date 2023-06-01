while ($row = mysqli_fetch_row($sign_in)) {
        print_r($row);
        echo "<br>";
    }
<?php
      $db = mysqli_connect("localhost", "root", "sks0hn01!!", "product-purchase-history-management");
      if (mysqli_connect_errno()) {
         echo "Error: Could not connect to database server.";
         exit;
      }
      // 4: 상품명, 2: 가격
      $sql = "SELECT * FROM product WHERE PINFO='TOP'";
      $result = mysqli_query($db, $sql);
      $cnt = 0;
      while ($row = mysqli_fetch_row($result)){
         echo "<tr>";
         echo "<td></td><td>$row[4]</td><td>$row[2]</td><td><button type='submit' name='cart1.(string)$cnt.' onclick=location.href='order.php?cart=<?$_POST[cart]?>'>카트 담기</button></td><td><button type='submit' name='order1.(string)$cnt.'>주문하기</button></td>";
         echo "<tr>";
         $cnt++;
      }
?>