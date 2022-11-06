const colors =['red', 'blue', 'green']

const printClr = function (color) {
  console.log(color)
}

// 1 forEach
colors.forEach(printClr)


colors.forEach(function (color) {
  console.log(color)
})

colors.forEach((color) => {
  console.log(color)
})


// reduce
const numbers = [90, 80, 70, 100]

const sumNum1 = numbers.reduce(function (result, number) {
  console.log(result)
  return result + number
})

console.log(sumNum1)

const sumNum2 = numbers.reduce((result, number) => {
  console.log(result)
  return result + number
}, 0)

console.log(sumNum2)