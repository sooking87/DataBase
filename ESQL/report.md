## 상품 구매 내역 조회 테이블 생성

### customer table

```sql
CREATE SCHEMA `Product-Purchase-History-Management` ;

CREATE TABLE `product-purchase-history-management`.`customer` (
  `CusID` VARCHAR(45) NOT NULL,
  `CusNAME` VARCHAR(45) NOT NULL,
  `AGE` INT NOT NULL,
  `PhoneNUM` CHAR(15) NULL,
  `CITY` VARCHAR(45) NOT NULL,
  `SEX` CHAR(10) NOT NULL,
  PRIMARY KEY (`CusID`));

insert into `Product-Purchase-History-Management`.`customer` values('C1', 'Smith', 20, '011-1111-1111', '영등포구', 'MALE');
insert into `Product-Purchase-History-Management`.`customer` values('C2', 'Jones', 18, '011-2222-2222', '용산구', 'MALE');
insert into `Product-Purchase-History-Management`.`customer` values('C3', 'Blake', 30, '011-3333-3333', '분당구', 'FEMALE');
insert into `Product-Purchase-History-Management`.`customer` values('C4', 'Clark', 20, '011-4444-4444', '분당구', 'FEMALE');
insert into `Product-Purchase-History-Management`.`customer` values('sksohn01', 'sooking87', 23, '010-3809-7668', '용산구', 'FEMALE');
```

### purchase table

이 테이블의 경우는 고객 테이블과 상품 정보 테이블을 "구매" 라는 행위를 통해서 연결하는 것이므로 따로 PK는 필요하지 않고 고객 테이블의 PK와 상품 정보 테이블의 PK를 포함하고 있으면 된다.

```sql
CREATE SCHEMA `Product-Purchase-History-Management` ;

CREATE TABLE `product-purchase-history-management`.`purchase` (
  `PNO` CHAR(15) NOT NULL,
  `CusID` VARCHAR(45) NOT NULL,
  `SNO` CHAR(5) NOT NULL,
  `DATE` CHAR(20) NOT NULL);


insert into `Product-Purchase-History-Management`.`purchase` values('00-230524-2243', 'C1', 'S1', '2023-05-24-10:38');
insert into `Product-Purchase-History-Management`.`purchase` values('01-230522-1015', 'C2', 'S2', '2023-05-22-22:20');
insert into `Product-Purchase-History-Management`.`purchase` values('01-230522-1015', 'sksohn01', 'S1', '2023-05-27-23:45');
insert into `Product-Purchase-History-Management`.`purchase` values('00-230525-2354', 'sksohn01', 'S1', '2023-05-27-23:50');
```

### product table

```sql
CREATE SCHEMA `Product-Purchase-History-Management` ;

CREATE TABLE `product-purchase-history-management`.`product` (
  `PNO` CHAR(15) NOT NULL,
  `PINFO` VARCHAR(45) NOT NULL,
  `PRICE` INT NOT NULL,
  `CNT` INT NOT NULL,
  PRIMARY KEY (`PNO`),
  CHECK (`CNT` >= 0 and `CNT` <= 10000)
);

-- 뒤에 - 붙히고 등록 년월일시분 넣기
-- 상의: 00
insert into `Product-Purchase-History-Management`.`product` values('00-230523-1134', 'TOP', 15000, 32);
insert into `Product-Purchase-History-Management`.`product` values('00-230524-2239', 'TOP', 12000, 60);
insert into `Product-Purchase-History-Management`.`product` values('00-230524-2243', 'TOP', 23000, 45);
insert into `Product-Purchase-History-Management`.`product` values('00-230525-2348', 'TOP', 32000, 16);
insert into `Product-Purchase-History-Management`.`product` values('00-230525-2354', 'TOP', 16000, 26);
-- 하의: 01
insert into `Product-Purchase-History-Management`.`product` values('01-230519-1028', 'BOTTOM', 23000, 43);
insert into `Product-Purchase-History-Management`.`product` values('01-230519-1130', 'BOTTOM', 35000, 72);
insert into `Product-Purchase-History-Management`.`product` values('01-230521-2334', 'BOTTOM', 43000, 21);
insert into `Product-Purchase-History-Management`.`product` values('01-230521-2343', 'BOTTOM', 32000, 16);
insert into `Product-Purchase-History-Management`.`product` values('01-230522-1015', 'BOTTOM', 20000, 36);
insert into `Product-Purchase-History-Management`.`product` values('01-230523-1420', 'BOTTOM', 25000, 32);
insert into `Product-Purchase-History-Management`.`product` values('01-230523-1424', 'BOTTOM', 28000, 12);
insert into `Product-Purchase-History-Management`.`product` values('01-230524-2215', 'BOTTOM', 20000, 82);
-- 신발: 02
insert into `Product-Purchase-History-Management`.`product` values('02-230523-1134', 'SHOES', 45000, 32);
insert into `Product-Purchase-History-Management`.`product` values('02-230524-2239', 'SHOES', 32000, 42);
insert into `Product-Purchase-History-Management`.`product` values('02-230524-2243', 'SHOES', 23000, 37);
insert into `Product-Purchase-History-Management`.`product` values('02-230525-2348', 'SHOES', 56000, 16);
-- 패션소품: 03
insert into `Product-Purchase-History-Management`.`product` values('03-230522-1023', 'ACC', 8000, 14);
insert into `Product-Purchase-History-Management`.`product` values('03-230525-1148', 'ACC', 12000, 16);
```

### cart table

```sql
CREATE SCHEMA `Product-Purchase-History-Management` ;

CREATE TABLE `suppliers-parts-projects`.`cart` (
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

## HLL에서 필요한 API

- show_product_list(): 구매 가능한 상품을 반환하는 함수
- order(): 구매 버튼을 누르면 구매한 상품 리스트를 보여주고 주문을 처리하는 함수
- customer_info(): 회원 정보와 과거 주문 내역을 확인하는 함수
- sign_up(): 회원가입을 진행하는 함수
- resign(): 회원탈퇴를 진행하는 함수
