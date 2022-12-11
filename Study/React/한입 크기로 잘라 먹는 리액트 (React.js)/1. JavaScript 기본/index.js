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
let d = 5;
if (d >= 7) {
  console.log("7이상 입니다.");
} else if (d >= 5) {
  console.log("5이상 입니다.");
} else {
  console.log("5미만 입니다.");
}

let country = "ko";

if (country === "ko") {
  console.log("한국");
} else if (country === "cn") {
  console.log("중국");
} else if (country === "jp") {
  console.log("일본");
} else {
  console.log("미 분류");
}

switch (country) {
  case "ko":
    console.log("한국");
    break; // 조건이 맞으면 밑에 도 다 실행하므로 break를 걸어준다.
  case "cn":
    console.log("중국");
    break;
  case "jp":
    console.log("일본");
    break;
  case "uk":
    console.log("영국");
    break;
  default:
    // else
    console.log("미 분류");
    break;
}

let country2 = "uk";

switch (country2) {
  case "ko":
    console.log("한국");
    break; // 조건이 맞으면 밑에 도 다 실행하므로 break를 걸어준다.
  case "cn":
    console.log("중국");
    break;
  case "jp":
    console.log("일본");
    break;
  case "uk":
    console.log("영국");
    break;
  default:
    // else
    console.log("미 분류");
    break;
}

switch (country2) {
  case "ko":
    console.log("한국");
    break; // 조건이 맞으면 밑에 도 다 실행하므로 break를 걸어준다.
  case "cn":
    console.log("중국");
    break;
  case "jp":
    console.log("일본");
    break;
  case "uk":
    console.log("영국");
  default:
    // else
    console.log("미 분류");
}

// 함수
let width1 = 10;
let height1 = 30;
let area1 = width1 * height1;
console.log(area1);

// 함수 생성
function getArea() {
  let width = 10;
  let height = 20;

  let area = width * height;
  console.log(area);
} // 함수 선언식, 함수 선언 방식의 함수 생성
// 함수 호출
getArea();
console.log("함수 실행 완료");

// 함수 생성
function getArea1(width, height) {
  let area = width * height;
  // console.log(area);
  return area; // 값 반환
}
// 함수 호출
let result = getArea1(1, 200);
console.log("넓이 :", result);
console.log("함수 실행 완료");

// 함수 내부에서 선언된 변수는 함수 외부에서 호출 불가능 (지역변수)
// 함수 외부에서 선언한 변수는 함수 내부에서 접근 가능 (전역변수, 글로벌 변수)

// 함수 표현식 (변수 이름 없이 변수에 담아서 사용)
let hello = function () {
  return "안녕하세요 여러분";
};
const helloText = hello();
console.log(helloText);

// console.log(helloA());  표현식은 호이스팅이 일어나지 않음
console.log(helloB()); // 선언식은 호이스팅이 일어남

// 함수 표현식
let helloA = function () {
  return "안녕하세요 여러분";
}; // 선언 전에는 접근불가

// 함수 선언식
function helloB() {
  return "안녕하세요 여러분";
} // 함수 호이스팅이 일어남 (선언전에 접근가능)

// 화살표 함수
let helloC = () => "안녕하세요 C 여러분";
console.log(helloC());

// 콜백 함수
function checkMood(mood) {
  if (mood === "good") {
    // 기분이 좋을 때 하는 동작
    sing();
  } else {
    // 기분이 안 좋을 때 하는 동작
    cry();
  }
}

function cry() {
  console.log("ACTION :: CRY");
}

function sing() {
  console.log("ACTION :: SING");
}

function dance() {
  console.log("ACTION :: DANCE");
}

checkMood("good");
// 동작이 한정적이다. 고정된 동작

// 콜백함수 (유연한 동작)
function checkMoodCallback(mood, goodCallback, badCallback) {
  if (mood === "good") {
    // 기분이 좋을 때 하는 동작
    goodCallback();
  } else {
    // 기분이 안 좋을 때 하는 동작
    badCallback();
  }
}

checkMoodCallback("sad", sing, cry);
// 함수를 매개변수로 넘기는 것
// 힘수를 호출

// 객체
let person1 = new Object(); // 객체 생성자 방식
let person2 = {}; // 객체 리터럴 방식 - 사용

let person3 = {
  key1: "value1",
  key2: 777, // key, value 쌍으로 저장되는 데이터를 프로퍼티 라고 부른다. (객체 프로퍼티)
  key3: true,
  key4: [1, 2, 3],
  key5: undefined,
  key5: function () {}
}; // 객체 리터럴 방식
// 객체 프로퍼티 : 속성, 객체가 가지고 있는 데이터
// 프로퍼티는 어떤 자료형도 다 가능하다.

console.log(person3);

// 객체에서 프로퍼티를 꺼내서 사용

console.log(person3.key1); // .으로 속성 값에 접근
console.log(person3.key2);

let person4 = {
  name: "kim",
  age: 28
};
// 괄호, . 으로 속성 값에 접근가능
// 괄호 표기법을 사용할 때는 key를 문자열 형태로 넣어야한다.
// key를 문자열 형태로 넣지 않으면 key를 변수로 인식한다.

console.log(person4.name);
console.log(person4["age"]);

// 객체 프로퍼티 추가, 삭제
let person5 = {
  name: "kim", // 멤버
  age: 28, // 멤버
  say: function () {
    console.log("안녕");
  }, // 메서드 -> 방법
  introduce: function () {
    console.log(`안녕 나는 ${this.name}`);
    console.log(`안녕 나는 ${this["name"]}이야`);
  }
};
// 함수인 프로퍼티는 메서드라 부르고
// 함수가 아닌 프로퍼티는 멤버라 부른다.

/// . 표기법, [] 표기법으로 추가 가능
person5.location = "한국";
person5["gender"] = "여성";
// 수정
person5.name = "bu";
person5["age"] = 30;

console.log(person5);
// const person5 가능
// person5이라는 상수 자체를 수정하는 것이 아니라 person5이라는 상수가 갖는 객체를 수정하는 행위
// person5 = {} 로 새로운 객체를 대입 연산를 통해 할당하지 않으면 괜찮다.

// 삭제
// 비추
// delete person5.age;
delete person5["gender"];
console.log(person5);

person5.age = null;
console.log(person5);

person5.say();
person5["introduce"]();

console.log(person5);
console.log(`name : ${"name" in person5}`);
console.log(`age : ${"age" in person5}`);
console.log(`gender : ${"gender" in person5}`);

// 배열
let arr1 = new Array(); // 배열 생성자
let arr2 = []; //배열 리터럴

console.log(arr2);

let arr3 = [1, 2, 3, 4]; //배열 리터럴
console.log(arr3);

let arr4 = [1, "a", [1, 2, 3], true]; // 모든 자료형 가능
console.log(arr4);

let arr5 = [1, 2, 3, 4, 5]; //배열 리터럴
console.log(arr5[0]);
console.log(arr5[3]);
console.log(arr5[4]);
// 추가
arr5.push(6);
console.log(arr5);
arr5.push({});
console.log(arr5);

console.log(arr5.length); // 현재 배열의 길이

// 반복문
console.log("bu");
console.log("bu");
console.log("bu");
console.log("bu");
console.log("bu");

for (let i = 1; i <= 100; i++) {
  // 반복 수행할 명령
  console.log("kim");
}
// 배열 순회
let arr6 = ["a", "b", "c"];
for (let i = 0; i < arr6.length; i++) {
  // 반복 수행할 명령
  console.log(arr6[i]);
}

// 객체 순회
let person6 = {
  name: "kim",
  age: 28,
  tall: 180
};

const personKeys = Object.keys(person6);
console.log(personKeys);

// key 순회
for (let i = 0; i < personKeys.length; i++) {
  console.log(personKeys[i]);
}

for (let i = 0; i < personKeys.length; i++) {
  const curKey = personKeys[i];
  const curValue = person6[curKey];

  console.log(`${curKey} : ${curValue}`);
}

// value 순회
const personValues = Object.values(person6);

for (let i = 0; i < personValues.length; i++) {
  console.log(personValues[i]);
}

// 내장함수
// 배열 순회

const arr7 = [1, 2, 3, 4, 5];

// 콜백 함수 forEach
arr7.forEach((element) => console.log(element));

arr7.forEach(function (element) {
  console.log(element * 2);
});

// map
// 모든 요소를 순회하면서 연산하여 값을 따로 배열로 만들어서 반환한다.

const newArr1 = [];
arr7.forEach(function (element) {
  newArr1.push(element * 2);
});

console.log(newArr1);

const newArr2 = arr7.map((elm) => {
  return elm * 2;
});

console.log(newArr2);

// includes (===, !==) - true/false
// 값이 있는지 찾기
let number = 3;
arr7.forEach((element) => {
  if (element === number) {
    console.log(true);
  }
});

console.log(arr7.includes(number));

// indexOf
//존재하면 인데스 출력 (값이 없으면 -1 반횐)
console.log(arr7.indexOf(number));

// 객체 배열에서 원하는 요소 인덱스 찾기
const arr8 = [
  { color: "red" },
  { color: "black" },
  { color: "blue" },
  { color: "green" }
];
// 같은 요소가 있으면 가장 먼저 조건을 만족하는 인덱스 반환
console.log(
  arr8.findIndex((elm) => {
    return elm.color === "red";
  })
);
// 화살표 함수
console.log(arr8.findIndex((elm) => elm.color === "green"));

const idx = arr8.findIndex((elm) => {
  return elm.color === "blue";
});

console.log(arr8[idx]);

// find
// 조건에 일치하는 요소 가져오기
const element = arr8.find((elm) => {
  return elm.color === "blue";
});

console.log(element);

// filter
// 콜백함수가 true를 반환하는 모든 요소를 배열로 반환한다.
const arr9 = [
  { num: 1, color: "red" },
  { num: 2, color: "black" },
  { num: 3, color: "blue" },
  { num: 4, color: "green" },
  { num: 5, color: "blue" }
];

console.log(arr9.filter((elm) => elm.color === "blue"));

// slice
// 배열을 자른다
console.log(arr9.slice()); // 배열 그대로 반환
console.log(arr9.slice(0, 3)); // 배열 0~2 번 반환
console.log(arr9.slice(3)); // 배열 앞에서 부터 2개 반환

// concat
// 배열 붙이기
const arr10 = [
  { num: 1, color: "red" },
  { num: 2, color: "black" },
  { num: 3, color: "blue" }
];
const arr11 = [
  { num: 4, color: "green" },
  { num: 5, color: "blue" },
  { num: 6, color: "yellow" }
];

console.log(arr10.concat(arr11));

// 사전 순으로 정렬
let chars = ["나", "다", "가"];

chars.sort();
console.log(chars);

let numbers = [0, 1, 3, 2, 10, 30, 20];
// numbers.sort(); // 문자로 보고 사전 슌으로 정렬
// console.log(numbers);

// 비교함수를 만들어 넣기
const compare = (a, b) => {
  // 1. 같다.
  // 2. 크다.
  // 3. 작다.
  if (a > b) {
    // 크다
    return 1;
    //return -1; 내림차순
  }

  if (a < b) {
    // 작다.
    return -1;
    // return 1; 내림차순
  }

  // 같다
  return 0;
};

numbers.sort(compare);
console.log(numbers);

// 문자열 배열 이어서 문자열로 출력하기 (구분자)
const arr12 = ["bu", "님", "안녕하세요"];

console.log(arr12);
console.log(arr12.join());
console.log(arr12.join(" "));
console.log(arr12.join("??"));
