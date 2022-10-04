CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

SELECT first_name, age FROM users;

SELECT * FROM users;

-- pk 보기
SELECT rowid, first_name FROM users;

-- 정렬
SELECT first_name, age FROM users
ORDER BY age ASC;

SELECT first_name, age FROM users
ORDER BY age DESC;

SELECT first_name, age, balance FROM users
ORDER BY age ASC, balance DESC;

SELECT country FROM users;
-- 중복제거
SELECT DISTINCT country FROM users;
SELECT DISTINCT country FROM users
ORDER by country;

SELECT DISTINCT first_name, country FROM users;
SELECT DISTINCT first_name, country FROM users
ORDER BY country DESC;

-- filtering data
SELECT first_name, age, balance FROM users
WHERE age >= 30;

SELECT first_name, age, balance FROM users
WHERE age >= 30 and balance > 500000;

-- like
SELECT first_name, last_name FROM users
WHERE first_name LIKE '%호%';

SELECT first_name, last_name FROM users
WHERE first_name LIKE '%준';

SELECT first_name, phone FROM users
WHERE phone LIKE '02-%';

SELECT first_name, age FROM users
WHERE age LIKE '2_';

SELECT first_name, phone FROM users
WHERE phone LIKE '%-51__-%';

-- in / not in
SELECT first_name, country FROM users
WHERE country IN ('경기도', '강원도');

SELECT first_name, country FROM users
WHERE country = '경기도' OR country = '강원도';

SELECT first_name, country FROM users
WHERE country NOT IN ('경기도', '강원도');

-- between
SELECT first_name, age FROM users
WHERE age BETWEEN 20 AND 30;

SELECT first_name, age FROM users
WHERE age >= 20 AND age <= 30;

SELECT first_name, age FROM users
WHERE age NOT BETWEEN 20 AND 30;

SELECT first_name, age FROM users
WHERE age < 20 OR age > 30;

-- limit
SELECT rowid, first_name FROM users
LIMIT 10;

SELECT first_name, balance FROM users
ORDER BY balance DESC LIMIT 10;

SELECT first_name, age FROM users
ORDER BY age LIMIT 5;

-- offest (앞에 띵구고 조회)
SELECT rowid, first_name FROM users
LIMIT 10 OFFSET 10;

-- group by (그룹별 묶음) / function 함께 사용
SELECT country, COUNT(*) FROM users
GROUP BY country;

SELECT country, COUNT(age) FROM users
GROUP BY country;
-- 별명 (컬럼 이름바꾸기)
SELECT last_name, COUNT(*) AS number_of_name FROM users
GROUP BY last_name;