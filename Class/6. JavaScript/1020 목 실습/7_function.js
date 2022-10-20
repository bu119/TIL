// 함수 옆 name는 디폴트 값

const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

console.log(greeting())
console.log(greeting('Kim'))