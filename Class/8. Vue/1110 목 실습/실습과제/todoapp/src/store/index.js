import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
			// 개별 todo Object
      {
        id: 1638771553377,                // nowDateObj.getTime()
        content: 'Vue',                   // Todo 내용
        dueDateTime: '2021-12-09T00:00',  // 마감일
        isCompleted: false,               // 완료된 할 일
        isImportant: true,				        // 중요 할 일
      },
      {
        id: 1638771553378,
        content: 'Vue Router',
        dueDateTime: '2021-12-10T00:00',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 16387715533779,
        content: 'Vuex',
        dueDateTime: '2021-12-11T00:00',
        isCompleted: true,
        isImportant: false,
      },
    ],
  },
  getters: {
    importantTodo(state){
      const importanttodo = state.todos.filter((todo) => {
        return todo.isImportant == true
      })
      return importanttodo
    }
  },
  mutations: {
    CREATE_TODO(state, todo){
      state.todos.push(todo)
    },
    TOGGLE_COMPLETED(state, todo){
      if (todo.isCompleted === true){
        todo.isCompleted = false
      } else {
        todo.isCompleted = true
      }
      return todo
    },
    TOGGLE_IMPORTANT(state, todo){
      if (todo.isImportant === true){
        todo.isImportant = false
      } else {
        todo.isImportant = true
      }
      return todo
    },


  },
  actions: {
    createTodo(context, content){

      const year = new Date().getFullYear()
      const month = new Date().getMonth()
      const day = new Date().getDate()
      const dueDate = new Date(year, month, day + 1)

      const todo = {
        id: new Date().getTime(),
        content,
        dueDateTime: dueDate,
        isCompleted: false,
        isImportant: false,
      }
      context.commit('CREATE_TODO', todo)
    }
  },
  modules: {
  }
})
