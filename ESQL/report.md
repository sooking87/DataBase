## 상품 구매 내역 조회 테이블 생성

### customer table

```sql
CREATE SCHEMA `Product-Purchase-History-Management` ;

CREATE TABLE `product-purchase-history-management`.`customer` (
  `CusID` VARCHAR(45) NOT NULL,
  `CusPW` VARCHAR(45) NOT NULL,
  `CusNAME` VARCHAR(45) NOT NULL,
  `AGE` INT NOT NULL,
  `PhoneNUM` CHAR(15) NULL,
  `CITY` VARCHAR(45) NOT NULL,
  `SEX` CHAR(10) NOT NULL,
  PRIMARY KEY (`CusID`));

insert into `Product-Purchase-History-Management`.`customer` values('C1', '111', 'Smith', 20, '011-1111-1111', '영등포구', 'MALE');
insert into `Product-Purchase-History-Management`.`customer` values('C2', '222', 'Jones', 18, '011-2222-2222', '용산구', 'MALE');
insert into `Product-Purchase-History-Management`.`customer` values('C3', '333', 'Blake', 30, '011-3333-3333', '분당구', 'FEMALE');
insert into `Product-Purchase-History-Management`.`customer` values('C4', '444', 'Clark', 20, '011-4444-4444', '분당구', 'FEMALE');
insert into `Product-Purchase-History-Management`.`customer` values('sksohn01', 'sks0hn01!!', 'sooking87', 23, '010-3809-7668', '용산구', 'FEMALE');
```

### purchase table

이 테이블의 경우는 고객 테이블과 상품 정보 테이블을 "구매" 라는 행위를 통해서 연결하는 것이므로 따로 PK는 필요하지 않고 고객 테이블의 PK와 상품 정보 테이블의 PK를 포함하고 있으면 된다.

```sql
CREATE SCHEMA `Product-Purchase-History-Management` ;

CREATE TABLE `product-purchase-history-management`.`purchase` (
  `PNO` CHAR(15) NOT NULL,
  `CusID` VARCHAR(45) NOT NULL,
  `DATE` CHAR(20) NOT NULL);


insert into `Product-Purchase-History-Management`.`purchase` values('00-230524-2243', 'C1', '2023-05-24-10:38');
insert into `Product-Purchase-History-Management`.`purchase` values('01-230522-1015', 'C2', '2023-05-22-22:20');
insert into `Product-Purchase-History-Management`.`purchase` values('01-230522-1015', 'sksohn01', '2023-05-27-23:45');
insert into `Product-Purchase-History-Management`.`purchase` values('00-230525-2354', 'sksohn01', '2023-05-27-23:50');
```

### product table

```sql
CREATE SCHEMA `Product-Purchase-History-Management` ;

CREATE TABLE `product-purchase-history-management`.`product` (
  `PNO` CHAR(15) NOT NULL,
  `PINFO` VARCHAR(45) NOT NULL,
  `PRICE` INT NOT NULL,
  `CNT` INT NOT NULL,
  `PNAME` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`PNO`),
  CHECK (`CNT` >= 0 and `CNT` <= 10000)
);

-- 뒤에 - 붙히고 등록 년월일시분 넣기
-- 상의: 00
insert into `Product-Purchase-History-Management`.`product` values('00-230523-1134', 'TOP', 15000, 32, '하트넥 셔링 골지 크롭 반팔 니트');
insert into `Product-Purchase-History-Management`.`product` values('00-230524-2239', 'TOP', 12000, 60, '셔링 단가라 크롭 반팔');
insert into `Product-Purchase-History-Management`.`product` values('00-230524-2243', 'TOP', 23000, 45, '시스루 오버핏 셔츠');
insert into `Product-Purchase-History-Management`.`product` values('00-230525-2348', 'TOP', 32000, 16, '홀터 니트');
insert into `Product-Purchase-History-Management`.`product` values('00-230525-2354', 'TOP', 16000, 26, '레이스 단추 브이넥');
-- 하의: 01
insert into `Product-Purchase-History-Management`.`product` values('01-230519-1028', 'BOTTOM', 23000, 43, '롱 와이드 팬츠');
insert into `Product-Purchase-History-Management`.`product` values('01-230519-1130', 'BOTTOM', 35000, 72, '쿨링 밴딩 팬츠');
insert into `Product-Purchase-History-Management`.`product` values('01-230521-2334', 'BOTTOM', 43000, 21, '허리 라벨 일자핏 팬츠');
insert into `Product-Purchase-History-Management`.`product` values('01-230521-2343', 'BOTTOM', 32000, 16, '포켓 와이드 트랙 팬츠');
insert into `Product-Purchase-History-Management`.`product` values('01-230522-1015', 'BOTTOM', 20000, 36, '투웨이 와이드 카고 팬츠');
insert into `Product-Purchase-History-Management`.`product` values('01-230523-1420', 'BOTTOM', 25000, 32, '빈티지 워싱 데님 숏팬츠');
insert into `Product-Purchase-History-Management`.`product` values('01-230523-1424', 'BOTTOM', 28000, 12, '하이웨스트 청반바지');
insert into `Product-Purchase-History-Management`.`product` values('01-230524-2215', 'BOTTOM', 20000, 82, '알렉산더 맥퀸 반바지');
-- 신발: 02
insert into `Product-Purchase-History-Management`.`product` values('02-230523-1134', 'SHOES', 45000, 32, '통굽 뮬');
insert into `Product-Purchase-History-Management`.`product` values('02-230524-2239', 'SHOES', 32000, 42, '샘플 스트랩 밴딩 샌들');
insert into `Product-Purchase-History-Management`.`product` values('02-230524-2243', 'SHOES', 23000, 37, '밴딩 통굽 샌들');
insert into `Product-Purchase-History-Management`.`product` values('02-230525-2348', 'SHOES', 56000, 16, '초경량 쪼리');
-- 패션소품: 03
insert into `Product-Purchase-History-Management`.`product` values('03-230522-1023', 'ACC', 8000, 14, '두줄 레이어드 목걸이');
insert into `Product-Purchase-History-Management`.`product` values('03-230525-1148', 'ACC', 12000, 16, '하트 오픈 링');
```

### cart table

```sql
CREATE SCHEMA `Product-Purchase-History-Management` ;

CREATE TABLE `Product-Purchase-History-Management`.`cart` (
  `CusID` VARCHAR(45) NOT NULL,
  `PNO` CHAR(15) NOT NULL,
  `InDATE` CHAR(20) NOT NULL);

insert into `Product-Purchase-History-Management`.`cart` values('C1', '00-230523-1134', '2023-05-24-9:38');
insert into `Product-Purchase-History-Management`.`cart` values('C1', '00-230524-2239', '2023-05-24-9:45');
insert into `Product-Purchase-History-Management`.`cart` values('C1', '01-230519-1028', '2023-05-25-21:45');
insert into `Product-Purchase-History-Management`.`cart` values('C2', '00-230525-2348', '2023-05-22-9:38');
insert into `Product-Purchase-History-Management`.`cart` values('C2', '01-230523-1420', '2023-05-23-9:45');
insert into `Product-Purchase-History-Management`.`cart` values('C2', '02-230524-2243', '2023-05-23-20:20');
insert into `Product-Purchase-History-Management`.`cart` values('C2', '03-230522-1023', '2023-05-25-21:45');
insert into `Product-Purchase-History-Management`.`cart` values('C3', '02-230524-2239', '2023-05-23-18:20');
insert into `Product-Purchase-History-Management`.`cart` values('C3', '03-230525-1148', '2023-05-25-23:53');
insert into `Product-Purchase-History-Management`.`cart` values('sksohn01', '00-230525-2348', '2023-05-23-20:20');
insert into `Product-Purchase-History-Management`.`cart` values('sksohn01', '01-230522-1015', '2023-05-26-21:10');
insert into `Product-Purchase-History-Management`.`cart` values('sksohn01', '02-230524-2239', '2023-05-26-21:20');
insert into `Product-Purchase-History-Management`.`cart` values('sksohn01', '03-230525-1148', '2023-05-27-23:53');
```

### deliveryperson TABLE

```sql
CREATE TABLE `product-purchase-history-management`.`deliveryperson` (
  `DNO` CHAR(5) NOT NULL,
  `DNAME` VARCHAR(45) NOT NULL,
  `DPhoneNUM` CHAR(15) NOT NULL,
  PRIMARY KEY (`DNO`));

insert into `Product-Purchase-History-Management`.`deliveryperson` values('D111', '돌비', '010-0000-1111');
insert into `Product-Purchase-History-Management`.`deliveryperson` values('D222', '한씨', '010-1111-2222');
insert into `Product-Purchase-History-Management`.`deliveryperson` values('D333', '손씨', '010-2222-3333');
insert into `Product-Purchase-History-Management`.`deliveryperson` values('D444', '윤씨', '010-3333-4444');
insert into `Product-Purchase-History-Management`.`deliveryperson` values('D555', '이씨', '010-4444-5555');
insert into `Product-Purchase-History-Management`.`deliveryperson` values('D666', '최씨', '010-5555-6666');
insert into `Product-Purchase-History-Management`.`deliveryperson` values('D777', '동꼬', '010-6666-7777');
insert into `Product-Purchase-History-Management`.`deliveryperson` values('D888', '아스라', '010-7777-8888');
insert into `Product-Purchase-History-Management`.`deliveryperson` values('D999', '레몬과자', '010-8888-9999');
insert into `Product-Purchase-History-Management`.`deliveryperson` values('D000', '백뭉', '010-9999-0000');
```
## HLL에서 필요한 API

- show_product_list(): 구매 가능한 상품을 반환하는 함수
- order(): 구매 버튼을 누르면 구매한 상품 리스트를 보여주고 주문을 처리하는 함수
- customer_info(): 회원 정보와 과거 주문 내역을 확인하는 함수
- sign_up(): 회원가입을 진행하는 함수
- resign(): 회원탈퇴를 진행하는 함수

```sql
-- UPDATE purchase SET DNO = 'D333' WHERE CusID = 'sksohn01';

-- DELETE FROM cart WHERE cart.PNO='00-230525-2348' AND cart.CusID='sksohn01'

-- UPDATE product SET CNT=20 WHERE PNO='00-230523-1134'

-- INSERT INTO `Product-Purchase-History-Management`.`purchase` (`PNO`, `CusID`, `DNO`, `DATE`) VALUES(%s %s %s %s)
```