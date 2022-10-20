// for in
// object 순회 할 때

// 키 값에 '' 없어도 스트링 값을 본다.
const fruits = {
  a: 'apple',
  b: 'banana',
}

for (const key in fruits) {
  console.log(key)
  console.log(fruits[key])
}