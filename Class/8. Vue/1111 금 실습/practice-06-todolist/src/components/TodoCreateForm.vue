<template>
  <form @submit="createTodo">
    <button class="btn">
      <i class="bi bi-plus-lg"></i>
    </button>
    <input
      type="text"
      v-model="content"
      class="form-control"  
      placeholder="할 일을 작성해주세요!"
      required
    >
  </form>
</template>

<script>
export default {
  data() {
    return {
      content: '',
    }
  },
  methods: {
    createTodo(event) {
      event.preventDefault()
      const data = {
        content: this.content,
      }
      if (this.$route.name === 'ImportantTodoPage') {
        this.$store.dispatch('todo/createImportantTodo', data)
      } else {
        this.$store.dispatch('todo/createTodayTodo', data)
      }
      this.content = ''
    }
  }
}
</script>

<style scoped>
form {
  display: flex;
}
</style>