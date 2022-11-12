<template>
  <div>
    <form @submit.prevent="createTodo">
      <button class="btn"><i class="bi bi-plus-lg"></i></button>
      <input type="text" v-model.trim="content" placeholder="할 일을 작성해주세요!" class="form-control">
    </form>
  </div>
</template>

<script>
export default {
  name:'TodoCreateForm',
  data(){
    return {
      content: null,
    }
  },
  methods: {
    createTodo() {
      const content = this.content
      this.$store.dispatch('createTodo', content)
      // this.$router.push({ name: 'index' })
    }
  }

}
</script>

<style>
form {
  display: flex;
}
</style>