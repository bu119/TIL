// for of

// object를 제외한 반복 가능한 객체를 순회 할 때 사용
// array, set, ...

const numbers = [100, 200, 300]

for (const number of numbers) {
  console.log(number)
}


// in 으로 바꾸면 키 값이 나온다.
for (const number in numbers) {
  console.log(number)
}

// 근데 in으로 할꺼면 이렇게 쓰지!! 저렇게 안씀
for (const i in numbers) {
  console.log(i)
  console.log(numbers[i])
}