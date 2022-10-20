const noArgs = function () {
  return 0
}

console.log(noArgs(1, 2, 3))

// 매개변수와 인자의 개수 불일치 허용
// 2. 매개변수보다 인자의 개수가 많을 때
const towArgs = function (arg1, arg2) {
  return [arg1, arg2]
}

console.log(towArgs(1, 2, 3))

// 1. 매개변수보다 인자의 개수가 적을 때
const threeArgs = function (arg1, arg2, arg3) {
  return [arg1, arg2, arg3]
}

console.log(threeArgs())
console.log(threeArgs(1))
console.log(threeArgs(1, 2))
