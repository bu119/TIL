const obj = {
  greeting: function () {
    console.log('hi')
  }

}

obj.greeting()


const obj2 = {
  greeting() {
    console.log('hi')
  }

}

obj2.greeting()