const arr = [1, 2, 3, 4, 5]
const result = arr.some((elem) => {
  return elem % 2 === 0
})

console.log(result)