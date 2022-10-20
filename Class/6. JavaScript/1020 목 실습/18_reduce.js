const tests = [90, 90, 80, 77]

// 총합
const sum = tests.reduce((acc, element) => {
  console.log(acc)
  return acc + element
}, 0) 
// 초기값 0
console.log(sum)

// 평균
const avg = tests.reduce((acc, element) => {
  return acc + element
}, 0) / tests.length

console.log(avg)