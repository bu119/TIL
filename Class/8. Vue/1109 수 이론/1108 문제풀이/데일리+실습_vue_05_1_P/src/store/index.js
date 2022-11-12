import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: JSON.parse(sessionStorage.getItem('orderList')) || [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: true,
        image: 'https://source.unsplash.com/featured/?americano'
      },
      { 
        title: '라떼',
        price: 4000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?latte',
      },
      { 
        title: '카푸치노',
        price: 4500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?capucchino',
      },
    ],
    sizeList: [
      {
        name: 'small',
        price: 0,
        selected: true,
      },
      {
        name: 'medium',
        price: 500,
        selected: false,
      },
      {
        name: 'large',
        price: 1000,
        selected: false,
      },
    ],
    optionList: [
      {
        type: '샷',
        price: 500,
        count: 0,
      },
      {
        type: '바닐라 시럽',
        price: 500,
        count: 0,
      },
      {
        type: '카라멜 시럽',
        price: 500,
        count: 0,
        },
    ],
    
  },
  getters: {
    totalOrderCount(state){
      return state.orderList.length
    },

    totalOrderPrice(state){
      return state.orderList.reduce((acc, order) =>{
        const price = order.menu.price
        const size = order.size.price
        const option = order.option.reduce((acc, op) => (op.count > 0) ? acc+op.price : acc+0, 0)
        return acc + price + size + option
      }, 0)
    },

  },
  mutations: {
    addOrder: function (state) {
      let selectedMenu = {}
      let selectedSize = {}

      state.menuList.forEach(menu => {
        if (menu.selected){
          selectedMenu = menu
        }
      })

      state.sizeList.forEach(size => {
        if (size.selected){
          selectedSize = size
        }
      })

      const option = state.optionList

      const order = {
        menu: selectedMenu,
        size: selectedSize,
        option: option,
      }
      // console.log(order)
      state.orderList.push(order)
      sessionStorage.setItem('orderList', JSON.stringify(state.orderList))


    },
    updateMenuList: function (state, selectedMenu) {
      console.log(selectedMenu)
      for(let i=0; i < state.menuList.length; i++){
        const menu = state.menuList[i]
        if(menu.title === selectedMenu.title){
          menu.selected = true
        }else{
          menu.selected = false
        }
      }
    },
    updateSizeList: function (state, selectedSize) {
      for(let i=0; i< state.sizeList.length; i++){
        const size = state.sizeList[i]
        if(size.name === selectedSize.name){
          size.selected = true
        }else{
          size.selected = false
        }
      }
    },
    updateOptionList(state, newOption) {
      const newOptions = []
      state.optionList.forEach(option => {
        if(option.type === newOption.type){
          // console.log(option.type, newOption.type)
          newOptions.push(newOption)
        }
        else{
          newOptions.push(option)
        }
      })

      state.optionList = newOptions
    }

  },
  actions: {
  },
  modules: {
  }
})