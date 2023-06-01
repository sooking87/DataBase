
<?php
error_reporting(E_ALL);

ini_set('display_errors', '1');
$db = mysqli_connect("localhost", "root", "Min02choi!", "meal_kit_market");
if (mysqli_connect_errno()) {
    echo "Error: Could not connect to database server.";
    exit;
}
$sql = "SELECT cno, name FROM customer";
$result = mysqli_query($db, $sql);
// php에서 사용가능한 데이터 형태인 배열로 반환
;
//        echo $row;
//        print_r($row);
while ($row = mysqli_fetch_row($result)){
    echo "<tr>";
    echo "<td>$row[0]</td><td>$row[1]</td>";
    echo "<tr>";
}

// mysqli_close($db);
?>
