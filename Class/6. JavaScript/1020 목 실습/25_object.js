const jsObj = {
  coffee: 'Americano',
  iceCream: 'Cookie and cream',
}

// Object -> JSON
const ObjToJson = JSON.stringify(jsObj)
console.log(ObjToJson)
console.log(typeof ObjToJson)

// JSON -> Object
const JsonToObj = JSON.parse(ObjToJson)
console.log(JsonToObj)
console.log(typeof JsonToObj)
