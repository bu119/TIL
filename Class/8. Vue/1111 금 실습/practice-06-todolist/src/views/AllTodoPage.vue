<template>
  <div>
    <h1>모든 할일</h1>
    <TodoCreateForm />
    <hr>
    <TodoList :todos="allTodoList" />
  </div>
</template>

<script>
import TodoCreateForm from '../components/TodoCreateForm.vue'
import TodoList from '../components/TodoList.vue'

export default {
  components: {
    TodoCreateForm,
    TodoList,
  },
  computed: {
    allTodoList() {
      return this.$store.state.todo.list
    }
  }  
}
</script>

<style>

</style>