<template>
  <div id="main">
    <h1>모든 할일</h1>
    <br>
    <TodoCreateForm/>
    <hr>
    <TodoList/>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoCreateForm from '@/components/TodoCreateForm'

export default {
  name: 'AllTodoPageView',
  components: {
    TodoList,
    TodoCreateForm,
  },
} 
</script>

<style>

</style>