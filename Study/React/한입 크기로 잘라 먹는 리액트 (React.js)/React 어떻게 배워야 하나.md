## React 어떻게 배워야 하나?

- Javascript - Node.js - React.js



# JavaScript 기본

- 개발자 도구 open 단축키
  - F12
  - ctrl + shift + i



```javascript
console.log("hello");
console.log("신기하구먼");

let age = 25;
console.log(age); // 25

age = 30;
console.log(age);

// 1. 변수명 : 기호 사용 불가 (_ $ 사용가능)

let a_$ = 100;
console.log(a_$);

// 2. 변수명은 반드시 숫자가 아닌 문자로 시작!
// 3. 예약어 사용 불가 ex) if

// 변수 선언 let, var
// but, var 는 잘못된 동작이 많다. - 문제가 생길 가능성 up
// let을 사용

// 변하지 않는 값: 상수 - const
// 값 재할당 불가

// 원시타입 자료형
// 숫자형 (정수, 실수, 무한대, 연산실패)
let tall = 180.5; // 실수
let small = 150; // 정수
let inf = Infinity;
let minusInf = -Infinity;
let nan = NaN;
console.log(tall + small);
console.log(inf);
console.log(minusInf);

// 문자열
let name1 = "bu";
let name2 = "김부경";
let name3 = `your name ${name2}`;

console.log(name3);

// 불린형 (boolean)
let isSwichOff = false;

// null 의도적으로 사용
// undefined 자동으로 설정 (변수에 값 할당 안할 때)

// 자동형변환

let numA = 12;
let numB = "2";
console.log(numA * numB); // 숫자형으로 계산 (묵시적 형변환)
console.log(numA + numB); // 문자형으로 계산
console.log(numA + parseInt(numB)); // 문자형을 숫자형으로 의도적으로 형변환 (명시적 형변환)

// 연산자
let a = 10;
console.log(++a); // 10 // 앞에 붙으면 바로 적용
a = 10;
console.log(a++); // 10 // 뒤에 붙으면 다음부터 값 변화
console.log(a);

a = 10;
console.log(a--);
console.log(a);
a = 10;
console.log(--a);
console.log(--a);

// 논리 연산자
console.log(!true); // ! = not : 값을 반대로 바꿔준다.
console.log(!false);
console.log(true && true); // true AND true
console.log(true && false);
console.log(true || false); // true OR true
console.log(false || true);
console.log(false || false);

// 비교연산자
let compareA = 1 == "1"; // 값만 비교, 타입 비교 X
console.log(compareA);
let compareB = 1 === "1"; // 값 타입 모두 비교
console.log(compareB);

let compareC = 1 != "1"; // 값 타입 모두 비교
console.log(compareC);
let compareD = 1 !== "1"; // 값 타입 모두 비교
console.log(compareD);

// === 으로 비교!!!! (안전하다)
let compareE = 1 < 2;
console.log(compareE);
let compareF = 3 < 3;
console.log(compareF);
let compareG = 3 >= 3;
console.log(compareG);

let compareH = 7;
console.log(typeof compareH);
compareH = "7";
console.log(typeof compareH);

// null 병합 연산자
let b;

b = b ?? 10; // b가 null 또는 undefine 이면 (값이 없다면) 10을 대입해라.
console.log(b);

let c = 20;
c = c ?? 10; // c에 값이 있어서 변화 X
console.log(c);
```

​	

```javascript
console.log("hello");
console.log("신기하구먼");

let age = 25;
console.log(age); // 25

age = 30;
console.log(age);

// 1. 변수명 : 기호 사용 불가 (_ $ 사용가능)

let a_$ = 100;
console.log(a_$);

// 2. 변수명은 반드시 숫자가 아닌 문자로 시작!
// 3. 예약어 사용 불가 ex) if

// 변수 선언 let, var
// but, var 는 잘못된 동작이 많다. - 문제가 생길 가능성 up
// let을 사용

// 변하지 않는 값: 상수 - const
// 값 재할당 불가

// 원시타입 자료형
// 숫자형 (정수, 실수, 무한대, 연산실패)
let tall = 180.5; // 실수
let small = 150; // 정수
let inf = Infinity;
let minusInf = -Infinity;
let nan = NaN;
console.log(tall + small);
console.log(inf);
console.log(minusInf);

// 문자열
let name1 = "bu";
let name2 = "김부경";
let name3 = `your name ${name2}`;

console.log(name3);

// 불린형 (boolean)
let isSwichOff = false;

// null 의도적으로 사용
// undefined 자동으로 설정 (변수에 값 할당 안할 때)

// 자동형변환

let numA = 12;
let numB = "2";
console.log(numA * numB); // 숫자형으로 계산 (묵시적 형변환)
console.log(numA + numB); // 문자형으로 계산
console.log(numA + parseInt(numB)); // 문자형을 숫자형으로 의도적으로 형변환 (명시적 형변환)

// 연산자
let a = 10;
console.log(++a); // 10 // 앞에 붙으면 바로 적용
a = 10;
console.log(a++); // 10 // 뒤에 붙으면 다음부터 값 변화
console.log(a);

a = 10;
console.log(a--);
console.log(a);
a = 10;
console.log(--a);
console.log(--a);

// 논리 연산자
console.log(!true); // ! = not : 값을 반대로 바꿔준다.
console.log(!false);
console.log(true && true); // true AND true
console.log(true && false);
console.log(true || false); // true OR true
console.log(false || true);
console.log(false || false);

// 비교연산자
let compareA = 1 == "1"; // 값만 비교, 타입 비교 X
console.log(compareA);
let compareB = 1 === "1"; // 값 타입 모두 비교
console.log(compareB);

let compareC = 1 != "1"; // 값 타입 모두 비교
console.log(compareC);
let compareD = 1 !== "1"; // 값 타입 모두 비교
console.log(compareD);

// === 으로 비교!!!! (안전하다)
let compareE = 1 < 2;
console.log(compareE);
let compareF = 3 < 3;
console.log(compareF);
let compareG = 3 >= 3;
console.log(compareG);

let compareH = 7;
console.log(typeof compareH);
compareH = "7";
console.log(typeof compareH);

// null 병합 연산자
let b;

b = b ?? 10; // b가 null 또는 undefine 이면 (값이 없다면) 10을 대입해라.
console.log(b);

let c = 20;
c = c ?? 10; // c에 값이 있어서 변화 X
console.log(c);

// 조건문

```



```javascript
// Truthy & Falsy

let a = "";
if (a) {
  console.log("TRUE");
} else {
  console.log("FALSE");
}

a = "STRING";
if (a) {
  console.log("TRUE");
} else {
  console.log("FALSE");
}

// 빈배열 - 참
a = [];
if (a) {
  console.log("TRUE");
} else {
  console.log("FALSE");
}

a = 0;
if (a) {
  console.log("TRUE");
} else {
  console.log("FALSE");
}

// Falsy(false) - null, undefined, 0, -0, NaN, ""(빈문자열)

const getName1 = (person) => {
  return person.name;
};

let person1 = { name: "kim" };
const name1 = getName1(person1);
console.log(name1);

// 값이 undefined 이면
const getName2 = (person) => {
  if (person === undefined) {
    return "객체가 아닙니다.";
  }
  return person.name;
};

let person2;
const name2 = getName2(person2);
console.log(name2);

```

