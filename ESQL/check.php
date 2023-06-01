<?php
# db 접속
include_once('connect.php');

# form 데이터 읽어오기
$title = $_POST['title'];
$author = $_POST['author'];
$date = $_POST['date'];

echo "<h3>추가할 책의 제목은 ($title), 작가명은 ($author), 출판된 날짜는 $date</h3>";

# insert sql 작성
$sql = "INSERT INTO booklist (title, author, date) VALUES ($title, $author, $date)";

if ($conn->query($sql)) echo "<h3>도서등록 성공</h3>";
else echo "<h3>도서등록 실패</h3>";

?>