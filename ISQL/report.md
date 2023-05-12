## 1-1

```sql
SELECT SNO
FROM spj
WHERE JNO = "J1"
ORDER BY SNO;
```

## 1-2

```sql
SELECT PNO
FROM spj
WHERE QTY >= 300
AND QTY <= 750;
```

## 1-3

```sql
SELECT PNO
FROM supplier, project, spj
WHERE
    supplier.`SNO` = spj.`SNO`
    AND project.`JNO` = spj.`JNO`
    AND supplier.`CITY` = "London"
    AND project.`CITY` = "London";
```

## 1-4

```sql
SELECT
    supplier.`CITY`,
    project.`CITY`
FROM supplier, spj, project
WHERE
    supplier.`SNO` = spj.`SNO`
    AND project.`JNO` = spj.`JNO`;
```

## 2-1

```sql
SELECT PNO, JNO, SUM(QTY)
FROM spj
GROUP BY JNO, PNO;
```

## 2-2

```sql
SELECT PNO
FROM spj
GROUP BY PNO
HAVING AVG(QTY) >= 320;
```

## 2-3

```sql
SELECT JNO, CITY
FROM project
WHERE CITY LIKE '_o%';
```

## 2-4

```sql
SELECT JNO
FROM project
WHERE CITY = (
        SELECT CITY
        FROM project
        ORDER BY CITY
        LIMIT 1
    );
```

## 2-5

```sql
SELECT JNO
FROM spj
WHERE PNO = 'P1'
GROUP BY JNO
HAVING AVG(QTY) > (
        SELECT MAX(QTY)
        FROM spj
        WHERE JNO = "J1"
    );
```

## 3-1

```sql
SELECT PNO
FROM spj
WHERE EXISTS (
        SELECT *
        FROM project
        WHERE
            spj.`JNO` = project.`JNO`
            AND CITY = 'London'
    );
```

## 3-2

```sql
SELECT DISTINCT JNO
FROM project
WHERE JNO NOT IN (
        SELECT JNO
        FROM spj
        WHERE EXISTS (
                SELECT
                    DISTINCT JNO
                FROM
                    part,
                    supplier
                WHERE
                    part.`PNO` = spj.`PNO`
                    AND supplier.`SNO` = spj.`SNO`
                    AND COLOR = 'Red'
                    AND supplier.`CITY` = 'London'
            )
    );
```

## 3-3

```sql
SELECT JNO
FROM spj
WHERE EXISTS (
        SELECT *
        FROM supplier
        WHERE
            spj.`SNO` = supplier.`SNO`
            AND SNO = 'S1'
    );
```

## 3-4

```sql
(
    SELECT CITY
    FROM spj, supplier
    WHERE
        spj.`SNO` = supplier.`SNO`
)
UNION (
    SELECT CITY
    FROM spj, part
    WHERE
        spj.`PNO` = part.`PNO`
)
UNION (
    SELECT CITY
    FROM spj, project
    WHERE
        spj.`JNO` = project.`JNO`
)
ORDER BY CITY;
```

## 4-1

```sql
DELETE project
FROM project, part, spj
WHERE
    project.`JNO` = spj.`JNO`
    AND part.`PNO` = spj.`PNO`
    AND part.`PNO` IS NULL;
```

## 4-2

```sql
INSERT INTO
    `suppliers-parts-projects`.`supplier` (
        `SNO`,
        `SNAME`,
        `STATUS`,
        `CITY`
    )
VALUES (
        "S10",
        "Smith",
         NULL,
        "New York"
    );
```

# 4-3

```sql
CREATE TABLE table1 (
        SELECT PNO
        FROM spj, supplier
        WHERE
            supplier.`SNO` = spj.`SNO`
            AND supplier.`CITY` = "London"
    )
UNION (
    SELECT PNO
    FROM spj, project
    WHERE
        project.`JNO` = spj.`JNO`
        AND project.`CITY` = "London"
)
ORDER BY PNO;
```

# 4-4

```sql
CREATE TABLE table2 (
        SELECT JNO
        FROM spj, supplier
        WHERE
            supplier.`SNO` = spj.`SNO`
            AND supplier.`CITY` = "London"
    )
UNION (
    SELECT JNO
    FROM project
    WHERE
        project.`CITY` = "London"
)
ORDER BY JNO;
```

## 5-1

```sql
CREATE TABLE
    `suppliers-parts-projects`.`project-developer` (
        `PDNO` CHAR(4) NOT NULL,
        `PDNAME` VARCHAR(45) NOT NULL,
        `ING` CHAR(2) NOT NULL,
        PRIMARY KEY (`PDNO`)
    );

INSERT INTO
    `suppliers-parts-projects`.`project-developer` (`PDNO`, `PDNAME`, `ING`)
VALUES ("PD1", "Smith", "J1"), ("PD2", "Jones", "J1"), ("PD3", "Blake", "J2"), ("PD4", "Adams", "J2"), ("PD5", "Clark", "J2"), ("PD6", "Blake", "J3"), ("PD7", "Clara", "J4"), ("PD8", "Shara", "J5"), ("PD9", "JiYoon", "J6"), ("PD10", "Sohn", "J7");
```

## 5-2

```sql
CREATE INDEX idx_sno ON supplier (SNO);

CREATE INDEX idx_pno ON part (PNO);

CREATE INDEX idx_jno ON project (JNO);

SHOW INDEX FROM supplier;

SHOW INDEX FROM part;

SHOW INDEX FROM project
```

## 5-3

```sql
CREATE SCHEMA `wholesale` ;

CREATE TABLE `wholesale`.`supplier` (
  `SNO` CHAR(5) NOT NULL,
  `SNAME` VARCHAR(45) NOT NULL,
  `STATUS` INT NULL,
  `CITY` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`SNO`));

insert into `wholesale`.`supplier` values('S1', 'Smith', 20, 'London');
insert into `wholesale`.`supplier` values('S2', 'Jones', 10, 'Paris');
insert into `wholesale`.`supplier` values('S3', 'Blake', 30, 'Paris');
insert into `wholesale`.`supplier` values('S4', 'Clark', 20, 'London');
insert into `wholesale`.`supplier` values('S5', 'Adams', 30, 'Athens');


CREATE TABLE `wholesale`.`employee` (
  `ENO` CHAR(5) NOT NULL,
  `ENAME` VARCHAR(45) NOT NULL,
  `OFFICECODE` CHAR(5) NULL,
  PRIMARY KEY (`ENO`));

insert into `wholesale`.`employee` values('E1', 'Smith', 'O1');
insert into `wholesale`.`employee` values('E2', 'Jones', 'O1');
insert into `wholesale`.`employee` values('E3', 'Blake', 'O2');
insert into `wholesale`.`employee` values('E4', 'Clark', 'O2');
insert into `wholesale`.`employee` values('E5', 'Adams', 'O2');
insert into `wholesale`.`employee` values('E6', 'Clara', 'O3');
insert into `wholesale`.`employee` values('E7', 'Sohn', 'O4');
insert into `wholesale`.`employee` values('E8', 'Soo', 'O4');

  CREATE TABLE `wholesale`.`customer` (
  `CNO` CHAR(5) NOT NULL,
  `CUSNAME` VARCHAR(45) NOT NULL,
  `CITY` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CNO`));

insert into `wholesale`.`customer` values('C1', 'Choi', 'London');
insert into `wholesale`.`customer` values('C2', 'Lee', 'Paris');
insert into `wholesale`.`customer` values('C3', 'Yoon', 'Athens');
insert into `wholesale`.`customer` values('C4', 'Han', 'Rome');
insert into `wholesale`.`customer` values('C5', 'Park', 'Athens');
insert into `wholesale`.`customer` values('C6', 'Eun', 'London');
insert into `wholesale`.`customer` values('C7', 'Joo', 'Paris');
insert into `wholesale`.`customer` values('C8', 'Yil', 'Oslo');
```
