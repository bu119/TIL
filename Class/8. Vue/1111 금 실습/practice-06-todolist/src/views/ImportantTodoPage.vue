<template>
  <div>
    <h1>중요 할일</h1>
    <TodoCreateForm />
    <hr>
    <TodoList :todos="importantTodoList"/>
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
    importantTodoList() {
      return this.$store.getters['todo/importantTodoList']
    }
  }
}
</script>

<style>

</style>