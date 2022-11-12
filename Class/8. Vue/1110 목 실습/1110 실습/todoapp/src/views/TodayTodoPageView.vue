<template>
  <div id="main">
    <h1>오늘 할일</h1>
    <br>
    <TodoCreateForm/>
    <hr>
  </div>
</template>

<script>
import TodoCreateForm from '@/components/TodoCreateForm'

export default {
  name: 'TodayTodoPageView',
  components: {
    TodoCreateForm
  }
}
</script>

<style>

</style>