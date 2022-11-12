<template>
  <ul>
    <TodoListItem
      v-for="todo in todos"
      :key="todo.id"
      :todo="todo"
    />
  </ul>
</template>

<script>
import TodoListItem from './TodoListItem.vue'

export default {
  components: {
    TodoListItem
  },
  props: {
    todos: {
      type: Array,
      required: true,
    }
  },
}
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}
</style>