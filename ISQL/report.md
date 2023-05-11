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
GROUP BY PNO, JNO;
```

## 2-2

```sql
SELECT PNO
FROM spj
GROUP BY PNO, JNO
HAVING AVG(QTY) >= 320;
```

## 2-3

```sql
SELECT JNO, CITY
FROM project
WHERE CITY LIKE '_o%'
```

## 2-4

```sql
SELECT JNO
FROM project
WHERE CITY IN (
        SELECT JNO
        FROM project
        ORDER BY CITY LIMIT 1
    )
```

## 2-5

```sql

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
SELECT JNO
FROM spj
WHERE NOT EXISTS (
        SELECT *
        FROM part
        WHERE
            part.`PNO` = spj.`PNO`
            AND COLOR = 'Red'
            AND CITY = 'London'
    )
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
    )
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
ORDER BY CITY
```
