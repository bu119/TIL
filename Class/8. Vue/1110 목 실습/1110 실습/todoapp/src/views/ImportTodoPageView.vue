<template>
  <div id="main">
    <h1>중요 할일</h1>
    <br>
    <TodoCreateForm/>
    <hr>
    <TodoListItem 
      v-for="todo in importanttodo"
      :key="todo.id"
      :todo=todo
    />
  </div>
</template>

<script>
import TodoCreateForm from '@/components/TodoCreateForm'
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'ImportTodoPageView',
  components: {
    TodoCreateForm,
    TodoListItem 

  },
  computed: {
    importanttodo() {
      return this.$store.getters.importanttodo
    }
  }
}
</script>

<style>

</style>