
/* 
  1. forEach 메서드를 활용해 모든 사용자들의 이름을 출력하시오.
  2. filter 메서드를 활용해 결혼한 사람들만 모아 married 상수에 할당하시오.
  3. find 메서드를 활용해 이름이 Tom인 사람만 tom 상수에 할당하시오.
  4. map 메서드를 활용해 모든 사용자에게 isAlive 키를 추가하고 true로 설정한 뒤, newUsers 상수에 할당하시오.
  5. reduce 메서드를 활용해 모든 사용자들의 계좌잔액을 totalBalance 상수에 할당하시오. (총합)
*/

const users = [
  { name: 'John', age: 31, isMarried: true, balance: 100, },
  { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
  { name: 'Ashley', age: 25, isMarried: true, balance: 300, },
  { name: 'Robert', age: 27, isMarried: false, balance: 400, },
  { name: 'Tom', age: 35, isMarried: true, balance: 500, },
]

// 1. forEach
// 리턴이 없는 메서드 - console을 안에서 찍어야한다.
// for (key) in : object o (키 값) 
// for (value) of : object x (벨류 값)
// .forEach(콜백함수)
// 형태: users.forEach(()=> {})
users.forEach((element)=> {
  console.log(element.name)
})

users.forEach((element)=> console.log(element.name))


// 2. filter
// === 타입, 이름 같아야한다. (일치) (되도록이면 3개 짜리 사용)
// == 는 형변환이 일어난다.
const married = users.filter((user) => {
  return user.isMarried === true
})

console.log(married)

const married1 = users.filter((user) => user.isMarried)
console.log(married1)

// 3. find
// 형태: const tom = users.find(()=> {})
const tom = users.find((element)=> {
  return element.name === 'Tom'
})

console.log(tom)

// 4. map
// 형태: const newUsers = users.map(() => {})
// 중괄호 안이 두줄이라서 생략 불가능
const newUsers = users.map((element) => {
  element.isAlive = true
  return element
})
console.log(newUsers)

// 5. reduce
// 형태: const totlaBalance = users.reduce((결과값, 누적 계산할 값)=>{}, 초기값)
const totlaBalance = users.reduce((acc, element) => {
  console.log(acc)
  return acc + element.balance
}, 0)

// 누적 합
console.log(totlaBalance)

// 평균
console.log(totlaBalance/users.length)



