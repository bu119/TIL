<template>
  <div>
    <TodoListItem
      v-for = "todo in todos"
      :key="todo.id"
      :todo="todo"
    />
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  computed: {
    todos(){
      return this.$store.state.todos
    }
  },
  components: {
    TodoListItem
  },
}
</script>

<style>

</style>