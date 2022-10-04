
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 입력 데이터의 순서가 틀리다. 이름, 음식, 무게, 키,나이 순으로 입력해야한다. 
INSERT INTO zoo VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

-- 2) rowid의 값이 중복된다. rowid는 pk값이므로 유일해야한다. (중복되지않는 다른 값을 입력해야한다.)
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(10, 'alligator', 'carnivore', 250, 50);

-- 3) weight의 Constraints가 NOT NULL이므로 컬럼 값이 항상 존재해야한다. (weight의 값도 입력해준다.)
INSERT INTO zoo (name, eat, age) VALUES
('dolphin', 'carnivore', 3);
