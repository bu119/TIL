<template>
  <div class="todo-list-item">
    <div class="todo-list-item__main"  @click="toggleEditMode">
      <label>
        <input type="checkbox" class="me-3 d-none" :checked="isCompleted" @change="toggleCompleted">
        <i v-if="isCompleted" class="bi bi-check-circle text-success h4 clickable"></i>
        <i v-else class="bi bi-circle h4 clickable"></i>
        <span class="ms-2 clickable">
          {{ content }}
        </span>
      </label>
      <button class="btn ms-auto" @click.stop="toggleImportant">
        <i v-if="isImportant" class="bi bi-star-fill fc-yellow" ></i>
        <i v-else class="bi bi-star fc-yellow"></i>
      </button>
    </div>
    <div v-if="editMode">
      <TodoUpdateForm :todo="todo" @toggle-edit-mode="toggleEditMode"/>
    </div>
  </div>
</template>

<script>
import TodoUpdateForm from './TodoUpdateForm.vue'

export default {
  components: {
    TodoUpdateForm,
  },
  props: {
    todo: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      editMode: false,
    }
  },
  methods: {
    toggleCompleted() {
      const data = {
        ...this.todo,
        isCompleted: !this.todo.isCompleted 
      }
      this.$store.dispatch('todo/updateTodo', data)
    },
    toggleImportant() {
      const data = {
        ...this.todo,
        isImportant: !this.todo.isImportant 
      }
      this.$store.dispatch('todo/updateTodo', data)
    },
    toggleEditMode() {
      this.editMode = !this.editMode
    },
  },
  computed: {
    content() {
      return this.todo.content
    },
    isCompleted() {
      return this.todo.isCompleted
    },
    isImportant() {
      return this.todo.isImportant
    }
  },
}
</script>

<style scoped>
.todo-list-item {
  position: relative;
}

.todo-list-item__main {
  margin: 1rem 0;
  padding: 1rem;
  display: flex;
  align-items: center;
  border: 1px solid #D1D5DB;
  border-radius: .5rem;
  cursor: pointer;
}

.fc-yellow {
  color: #FBBF24;
}

.clickable {
  cursor: pointer;
}
</style>