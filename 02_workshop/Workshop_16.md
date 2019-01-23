Workshop_15 

```sql
CREATE TABLE bands (
	id INTEGER,
    name TEXT,
    debut INTEGER
);
```

```sql
INSERT INTO bands (id, name, debut)
VALUES (1, 'Queen', 1973),(2, 'Coldplay', 1998),(3, 'MCR', 2001);
```

```sql
SELECT id, name FROM users;
```

```
SELECT name FROM users where debut < 2000;
```

------------------------------------------------------------------------

Workshop_16

```sql
ALTER TABLE bands
ADD COLUMN members INTEGER;
```

```sql
UPDATE bands
SET members=4
WHERE id=1;
UPDATE bands
SET members=5
WHERE id=2;
UPDATE bands
SET members=9
WHERE id=3;
```

```sql
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
2           Coldplay    1998        5         
3           MCR         2001        9         
```



```sql
UPDATE bands
SET members=5
WHERE id=3;
```

```sql
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
2           Coldplay    1998        5         
3           MCR         2001        5      
```



```sql
DELETE FROM bands
where id=2;
```

```sql
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
3           MCR         2001        5  
```

