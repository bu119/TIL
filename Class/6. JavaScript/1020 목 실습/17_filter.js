const products = [
  { name: 'cucumber', type: 'vegetable'},
  { name: 'banana', type: 'fruit'},
  { name: 'carrot', type: 'vegetable'},
  { name: 'apple', type: 'fruit'},
]

const fruits = products.filter((element) => {
  return element.type === 'fruit'
})

console.log(fruits)