## 상품 구매 내역 조회 테이블 생성

### customer table

```sql
CREATE SCHEMA `Product-Purchase-History-Management` ;

CREATE TABLE `Product-Purchase-History-Management`.`customer` (
  `CusID` VARCHAR(45) NOT NULL,
  `CusNAME` VARCHAR(45) NOT NULL,
  `AGE` INT NOT NULL,
  `PhoneNUM` CHAR(15) NULL, 
  PRIMARY KEY (`CusID`));

insert into `Product-Purchase-History-Management`.`customer` values('S1', 'Smith', 20, '011-1111-1111');
insert into `Product-Purchase-History-Management`.`customer` values('S2', 'Jones', 18, '011-2222-2222');
insert into `Product-Purchase-History-Management`.`customer` values('S3', 'Blake', 30, '011-3333-3333');
insert into `Product-Purchase-History-Management`.`customer` values('S4', 'Clark', 20, '011-4444-4444');
insert into `Product-Purchase-History-Management`.`customer` values('sksohn01', 'sooking87', 23, '010-3809-7668');
```

### purchase table

이 테이블의 경우는 고객 테이블과 상품 정보 테이블을 "구매" 라는 행위를 통해서 연결하는 것이므로 따로 PK는 필요하지 않고 고객 테이블의 PK와 상품 정보 테이블의 PK를 포함하고 있으면 된다. 

```sql
CREATE SCHEMA `Product-Purchase-History-Management` ;

CREATE TABLE `Product-Purchase-History-Management`.`purchase` (
  `PNO` CHAR(10) NOT NULL, -- 230523-1159 (년월일-시분)
  `CNO` VARCHAR(45) NOT NULL,
  `DATE` CHAR(20) NOT NULL, -- 2023-05-23-11:45 (yyyy-mm-dd-hh:mm)
  PRIMARY KEY (`PNO`));

insert into `Product-Purchase-History-Management`.`purchase` values('00-01', 'S1', '2023-05-24-10:38');
insert into `Product-Purchase-History-Management`.`purchase` values('01-03', 'S2', '2023-05-22-22:20');
insert into `Product-Purchase-History-Management`.`purchase` values('00-02', 'sksohn01', '2023-05-27-23:45'),
insert into `Product-Purchase-History-Management`.`purchase` values('01-02', 'sksohn01', '2023-05-27-23:50');
```

### purchase-information table

```sql
CREATE SCHEMA `Product-Purchase-History-Management` ;

CREATE TABLE `Product-Purchase-History-Management`.`purchase-information` (
  `PNO` CHAR(10) NOT NULL, -- 230523-1159 (년월일-시분)
  `PINFO` VARCHAR(45) NOT NULL, -- 구매 상품의 카테고리: 상의, 하의, 신발, 패션소품
  `PRICE` INT NOT NULL,
  'CNT' INT NOT NULL, 
  PRIMARY KEY (`PNO`),
  check ('CNT' >= 0 and 'CNT' <= 10000));

-- 신발: 02
-- 패션소품: 03
-- 뒤에 - 붙히고 등록 순대로 붙히기
-- 상의: 00
insert into `Product-Purchase-History-Management`.`purchase-information` values('00-01', 'TOP', 15000, 32);
insert into `Product-Purchase-History-Management`.`purchase-information` values('00-02', 'TOP', 12000, 60);
insert into `Product-Purchase-History-Management`.`purchase-information` values('00-03', 'TOP', 23000, 45);
insert into `Product-Purchase-History-Management`.`purchase-information` values('00-04', 'TOP', 32000, 16);
insert into `Product-Purchase-History-Management`.`purchase-information` values('00-05', 'TOP', 16000, 26);
-- 하의: 01
insert into `Product-Purchase-History-Management`.`purchase-information` values('01-01', 'BOTTOM', 15000, 32);
insert into `Product-Purchase-History-Management`.`purchase-information` values('01-02', 'BOTTOM', 12000, 60);
insert into `Product-Purchase-History-Management`.`purchase-information` values('01-03', 'BOTTOM', 23000, 45);
insert into `Product-Purchase-History-Management`.`purchase-information` values('01-04', 'BOTTOM', 32000, 16);
insert into `Product-Purchase-History-Management`.`purchase-information` values('01-05', 'BOTTOM', 16000, 26);

```