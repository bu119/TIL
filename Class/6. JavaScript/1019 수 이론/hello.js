// console.log('hello, javascript');

// 선언식
function add(num1 ,num2) {
  return num1 + num2
}

console.log(add(2,7))

// 표현식
const sub = function (num1, num2) {
  return num1 - num2
}

console.log(sub(2,7))

const greeting = function ( name = 'Anonmous') {
  return `hi, ${name}`
} 

console.log(greeting())