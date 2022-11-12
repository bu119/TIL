import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store'
  },
  getters: {
  },
  mutations: {
    CHANGE_MESSAGE(state, message){
      state.message = message
    }
  },
  actions: {
    changeMessage(context, message) {
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
  }
})
