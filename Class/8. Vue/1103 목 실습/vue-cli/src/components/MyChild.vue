<template>
  <div>
    <h1>This is my component</h1>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭</button>
    <input
      type="text"
      v-model="childInputData"
      @keyup.enter="childInput"
    >
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  data: function() {
    return {
      ChildInputData: null,
    }
  },
  methods: {
    ChildToParent() {
      this.$emit('child-to-parent', 'child data')
    },
    ChildInput() {
      this.$emit('child-input', this.ChildInputData)
      this.ChildInputData = ''
    }
  }
}
</script>

<style>

</style>