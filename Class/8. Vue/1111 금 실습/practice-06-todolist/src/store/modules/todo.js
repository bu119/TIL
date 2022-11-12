import { mockCreateTodayTodo, mockCreateImportantTodo } from '../../api'

const state = () => {
  return {
    list: [
      {
        id: 1638771553377,
        content: 'Vue',
        dueDateTime: '2021-12-11T16:05',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 1638771553378,
        content: 'Vue Router',
        dueDateTime: '2021-12-11T16:05',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 16387715533779,
        content: 'Vuex',
        dueDateTime: '2021-12-11T16:05',
        isCompleted: true,
        isImportant: false,
      },
    ],
  }
}

const getters = {
  importantTodoList(state) {
    return state.list.filter(todo => !todo.isCompleted && todo.isImportant)
  },
  todayTodoList(state) {
    return state.list.filter(todo => {
      const todoDueDateTime = new Date(todo.dueDateTime)
      const nowDateTime = new Date()
      const isSameYear = todoDueDateTime.getFullYear() === nowDateTime.getFullYear()
      const isSameMonth = todoDueDateTime.getMonth() === nowDateTime.getMonth()
      const isSameDate = todoDueDateTime.getDate() === nowDateTime.getDate() 
      return !todo.isCompleted && isSameYear && isSameMonth && isSameDate
    })
  },
}

const mutations = {
  addTodo(state, newTodo) {
    state.list.unshift(newTodo)
  },
  updateTodo(state, newTodo) {
    state.list = state.list.map(todo => {
      if (todo.id === newTodo.id) {
        return newTodo
      } else {
        return todo
      }
    })
  }
}

const actions = {
  createTodayTodo({ commit }, data) {
    const todo = mockCreateTodayTodo(data)
    commit('addTodo', todo)
  },
  createImportantTodo({ commit }, data) {
    const todo = mockCreateImportantTodo(data)
    commit('addTodo', todo)
  },
  updateTodo({ commit }, data) {
    commit('updateTodo', data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}