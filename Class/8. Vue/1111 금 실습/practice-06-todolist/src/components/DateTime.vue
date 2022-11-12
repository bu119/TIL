<template>
  <div>
    <input
      type="date"
      v-model="date"
      class="form-control"  
      required
    >
    <input
      type="time"
      v-model="time"
      class="form-control"
    >
  </div>
</template>

<script>
export default {
  data() {
    return {
      date: '',
      time: '',
    }
  }
}
</script>

<style>

</style>