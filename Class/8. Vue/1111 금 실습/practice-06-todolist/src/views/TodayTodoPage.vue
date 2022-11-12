<template>
  <div>
    <h1>오늘 할일</h1>
    <TodoCreateForm />
    <hr>
    <TodoList :todos="todayTodoList" />
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
    todayTodoList() {
      return this.$store.getters['todo/todayTodoList']
    }
  },
}
</script>

<style>

</style>