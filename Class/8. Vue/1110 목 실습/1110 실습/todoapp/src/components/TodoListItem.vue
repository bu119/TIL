<template>
  <div>
    <div class="todo-list-item">
      <!-- <label>
        <input type="checkbox" class="me-3 d-none" 
          :checked="isCompleted"
          @click='toggleCompleted'
        >
        <i v-if="isCompleted" class="bi bi-check-circle text-success h4 clickable"></i>
        <i v-else class="bi bi-circle h4 clickable"></i>
        <span class="ms-2 clickable">
          {{ todo.content }}
        </span>
      </label> -->
      <div>
        <span @click='toggleCompleted' >
          <input type="checkbox" class="me-3 d-none">
          <i :class="[todo.isCompleted ? 'bi bi-check-circle' : 'bi bi-circle']"></i>
        </span>
        <span class="ms-2 clickable">{{ todo.content }}</span>
      </div>

      <span @click='toggleImportant' >
        <input type="checkbox" class="me-3 d-none">
        <i :class="[todo.isImportant ? 'bi bi-star-fill text-warning' : 'bi bi-star']"></i>
      </span>

    </div>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object
  },
  methods: {
    toggleCompleted() {
      this.$store.commit('TOGGLE_COMPLETED', this.todo)
    },
    toggleImportant() {
      this.$store.commit('TOGGLE_IMPORTANT', this.todo)
    },
  }
}
</script>

<style>
.todo-list-item {
  margin: 1rem 0;
  padding: 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 1px solid #D1D5DB;
  border-radius: 0.5rem;
  cursor: pointer;

}
</style>