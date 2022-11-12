<template>
  <div>
    <h2>AppChild</h2>
    <input type="text" @change="onChildInputChange">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appData: String,
    parentData: String,
    childData: String,
  },
  methods: {
    onChildInputChange(event){
      //console.log(event)
      this.$emit('child-input-change', event.target.value)
    }
  }
}

</script>

<style>

</style>