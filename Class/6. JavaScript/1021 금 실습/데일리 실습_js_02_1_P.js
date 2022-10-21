
/* 
  1. 해당 코드를 template string 을 활용하여 리팩토링하시오.
  2. 해당 코드를 arrow function 으로 리팩토링하시오.
  3. 해당 코드의 메서드 introduce 를 function 키워드 없이 리팩토링하시오.
  4. 해당 코드를 key, value를 한번씩만 작성하도록 리팩토링하시오.
*/

// 1
const name = 'Tom'

console.log(`Hi, my name is ${name}`)


// 2
// 함수식의 단점 : 호이스팅이 일어난다. (선언되기 이전에 호출해도 돌아간다. - 함수 표현식으로 변경)
// 함수 표현식:
// 괄호안에 파라메타가 하나일 때 생략 가능
// 한줄짜리는 리턴, 중괄호도 생략 가능
const add = (x, y) => x + y

console.log(add(2, 3))


// 3
//object 형태
// 키 값을 주고 벨류값에 함수가 들어갈 수 있다.
// 키 값을 함수로 변경
const tom = {
  name: 'Tom',
  introduce() {
    console.log('Hi, my name is ' + this.name)
  }
}

tom.introduce()


// 4
// 축약하기

const url = 'https://test.com'
const data = { message: 'Hello World!' }

const request = { url, data }

console.log(request)