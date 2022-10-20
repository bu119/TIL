const avengers = [
  { name : 'Stark', age: 45},
  { name : 'Rogers', age: 32},
  { name : 'Thor', age: 40},
]

const avenger = avengers.find((element) => {
  return element.name === 'Stark'
})

console.log(avenger)