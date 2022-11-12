<template>
  <form @submit="updateTodo">
    <button class="btn btn-success">수정하기</button>
    <input type="text" v-model="content">
    <input type="datetime-local" v-model="dueDateTime">
  </form>
</template>

<script>
export default {
  props: {
    todo: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      content: '',
      dueDateTime: '',
    }
  },
  methods: {
    updateTodo(event) {
      event.preventDefault()
      const todo = {
        ...this.todo,
        content: this.content,
        dueDateTime: this.dueDateTime,
      }
      this.$store.dispatch('todo/updateTodo', todo)
      this.$emit('toggle-edit-mode')
    }
  },
  created() {
    this.content = this.todo.content
    this.dueDateTime = this.todo.dueDateTime
  }
}
</script>

<style scoped>
form {
  margin: .25rem 0;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  border: 1px solid #D1D5DB;
  background-color: #f0f9ff;
  border-radius: .5rem;
}

form input {
  width: 100%;
  padding: 1rem;
  margin-top: 1rem;
  border: 1px solid #D1D5DB;
  border-radius: .375rem;
}
</style>