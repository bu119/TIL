<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <input 
      type="text"
      @keyup.enter="changeMessage"
      v-model="inputData"
    >
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      inputData: null,
    }
  },
  components: {
  },
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
    }
  },
  computed: {
    message() {
      return this.$store.state.message
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
