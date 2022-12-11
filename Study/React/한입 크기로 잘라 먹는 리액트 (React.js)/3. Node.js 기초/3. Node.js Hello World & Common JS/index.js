// module 불러오기 작업
const calc = require("./calc");
// 내장함수 require를 사용해서 해당 위치의 calc.js를 불러옴

console.log(calc)
console.log(calc.add(1, 2));
console.log(calc.add(4, 5));
console.log(calc.sub(10, 2));