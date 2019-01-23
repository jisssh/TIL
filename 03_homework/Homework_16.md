#### 다음과 같은 스키마를 가지는 DB 테이블 friends 를 생성한다.

| id (INTEGER) | name (TEXT) | location (TEXT) |
| :----------: | :---------: | :-------------: |
|              |             |                 |

```sql
CREATE TABLE friends(
id INTEGER PRYMARY KEY, name TEXT, location TEXT)
```

해당 테이블에 다음과 같이 데이터를 입력한다.



#### 해당 테이블에 다음과 같이 데이터를 입력한다.

| id (INTEGER) | name (TEXT) | location (TEXT) |
| :----------: | :---------: | :-------------: |
|      1       |   Justin    |      Seoul      |
|      2       |    Simon    |    New York     |
|      3       |    Chang    |    Las Vegas    |
|      4       |    John     |     Sydney      |

```
INSERT INTO friends(id, name, location)
VALUES (1, 'Justin','Seoul'),
(2, 'Simon', 'New York'),
(3, 'Chang','Las Vegas'),
(4, 'John','Sydney');
```

```sql
id          name        location  
----------  ----------  ----------
1           Justin      Seoul     
2           Simon       New York  
3           Chang       Las Vegas 
4           John        Sydney   
```



#### 

#### 스키마를 다음과 같이 변경한다.

| id (INTEGER) | name (TEXT) | location (TEXT) | married (INTEGER) |
| :----------: | :---------- | :-------------: | ----------------- |
|              |             |                 |                   |

```sql
ALTER TABLE friends
ADD COLUMN married INTEGER;
```



#### 데이터를 다음과 같이 추가한다.

| id (INTEGER) | name (TEXT) | location (TEXT) | married (INTEGER) |
| :----------: | :---------: | :-------------: | :---------------: |
|      1       |   Justin    |      Seoul      |         1         |
|      2       |    Simon    |    New York     |         0         |
|      3       |    Chang    |    Las Vegas    |         0         |
|      4       |    John     |     Sydney      |         1         |

```sql
UPDATE friends SET married = 1 WHERE id=1;
UPDATE friends SET married = 0 WHERE id=2;                                             UPDATE friends SET married = 0 WHERE id=3;                 
UPDATE friends SET married = 1 WHERE id=4;                                             
```

```sql
id          name        location    married   
----------  ----------  ----------  ----------
1           Justin      Seoul       1         
2           Simon       New York    0         
3           Chang       Las Vegas   0         
4           John        Sydney      1  
```



#### 아래 동작을 수행하기 위한 SQL 을 각각 작성하세요.

> married 가 0 인 데이터를 모두 삭제한다.

| id (INTEGER) | name (TEXT) | location (TEXT) | married (INTEGER) |
| :----------: | :---------: | :-------------: | :---------------: |
|      1       |   Justin    |      Seoul      |         1         |
|      4       |    John     |     Sydney      |         1         |

```sql

```

```sql

```



#### 테이블을 삭제한다.

```sql
DROP TABLE friends
```



