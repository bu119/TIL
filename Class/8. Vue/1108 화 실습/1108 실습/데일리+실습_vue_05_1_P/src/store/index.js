import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
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
        image: 'https://source.unsplash.com/featured/?latte'
      },
      {
        title: '카푸치노',
        price: 4500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?capucchino'
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
        price: 600,
        count: 0,
      },
      {
        type: '카라멜 시럽',
        price: 700,
        count: 0,
      },
    ]

  },
  getters: {
  },
  mutations: {
    addOrder(state) {
      const orderMenu = state.menuList.find((element) => {
        return element.selected
      })

      const orderSize = state.sizeList.find((element) => {
        return element.selected
      })

      const order = {
        menu: orderMenu,
        size: orderSize
      }

      state.orderList.push(order)
    },

    updateMenuList(state, selectedMenu) {
      state.menuList.forEach((menu) => {
        if (menu === selectedMenu) {
          menu.selected = true
        } else {
          menu.selected = false
        }
      })
      // selectedMenu.selected = !selectedMenu.selected
    },

    updateSizeList(state, selectedSize) {
      state.sizeList.forEach((size) => {
        if (size === selectedSize) {
          size.selected = true
        } else {
          size.selected = false
        }
      })
      // selectedSize.selected = !selectedSize.selected
    },

    // updateOptionList(state, newOption) {
    //   state.optionList = state.optionList.map((option) => {
    //     if (option === newOption) {
    //       option.count > 0
    //     }
    //     return option
    //   })
    // },

    increase(state, optionCount){
      optionCount.count += 1
    },
    decrease(state, optionCount){
      if (optionCount.count > 0) {
        optionCount.count -= 1

      }
    }


  },
  actions: {
  },
  modules: {
  }
})