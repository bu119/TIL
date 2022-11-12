<template>
  <div>
    <span @click="updateSizeList">
      {{ size.name }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods: {
    updateSizeList() {
      this.$store.commit('updateSizeList', this.size)
    }
  }
}
</script>

<style>
</style>