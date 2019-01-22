1. 우리가 사용하는 SQLite 는 RDBMS 에 속한다. RDBMS 의 특징을 2가지만 작성하 세요.

   ```
   모든 데이터를 2차원 테이블로 표현
   상호 관련성을 가진 테이블(table)의 집합
   ```

2. True and False

   2.1. 모든 RDBMS 는 같은 SQL 문을 사용한다. [ T ] 

   2.2. SQL 에서 명령어는 대문자로 써야만 동작한다. [ F ] 

   2.3. 일반적인 SQL 문에서 명령어는 세미콜론(;) 으로 끝난다. [ T ] 

   2.4. SQLite 에서 dot(.) 으로 시작하는 명령어는 SQL 이 아니다. [ F ] 

   2.5. 한개의 DB 에는 한개의 테이블만 존재한다. [ F ]

3. 다음 코드의 실행결과로 나타나는 값을 작성하세요.

   ```sql
   sqlite>.nulvalue "NULL"
   sqlite> CREATE TABLE ssafy ( 
   …> id INTEGER, 
   …> location TEXT, 
   …> class INTEGER 
   …> ); 
   sqlite> INSERT INTO ssafy (id, location) 
   …> VALUES (1, ‘JEJU’); 
   sqlite> SELECT class FROM ssafy WHERE id=1;
   
   ```

   ```
   => NULL
   ```


