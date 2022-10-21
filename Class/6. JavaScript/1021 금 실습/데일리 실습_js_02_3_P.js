
/* 
  1. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
  2. Rest operator를 활용해 아래 코드를 리팩토링 하시오.
  3. Spread operator를 활용해 아래 코드를 리팩토링 하시오.
*/

// 1-1
// const {name, extension, size} = savedFile

const savedFile = {
  name: 'profile',
  extension: 'jpg',
  size: 29930
}
function fileSummary({name, extension, size}) {
    console.log(`The file ${name}.${extension} is size of ${size} bytes.`)
}

fileSummary(savedFile);


// 1-2
const data = {
  username: 'myName',
  password: 'myPassword',
  email: 'my@mail.com',
}

const {username, password, email} = data

console.log(username, password, email)


// 2
// numbers 의 타입은 배열
function addNumbers(...numbers) {
  // const numbers = [a, b, c, d, e]; 대신 Rest 파라메타
  return numbers.reduce((sum, number) => sum + number, 0)
}

console.log(addNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


// 3-1
// 얕은 복사
const defaultColors = ['red', 'green', 'blue'];
const favoriteColors = ['navy', 'black', 'gold', 'white']
const palette = [...defaultColors, ...favoriteColors]

console.log(palette)

// 3-2
// 딕셔너리 형태이므로 []이 아니라 {}를 사용한다.
const info1 = { name: 'Tom', age: 30 }
const info2 = { isMarried: true, balance: 3000 }
const fullInfo = {...info1, ...info2}

console.log(fullInfo)
