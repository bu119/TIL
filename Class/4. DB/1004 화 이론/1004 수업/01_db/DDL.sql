-- 테이블 생성 --
CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);

-- 테이블 수정 --
-- 이름 생성
ALTER TABLE contacts RENAME TO new_contacts;

-- 이름 변경
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

-- 추가
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;
-- 기존 데이터가 존재하면 문제 발생 (새로운 칸에 값이 없다.)
-- 기본값 지정
-- ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';

-- 컬럼 삭제
ALTER TABLE new_contacts DROP COLUMN address;

-- 테이블 삭제 --
DROP TABLE new_contacts;