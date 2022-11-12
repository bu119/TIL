<template>
  <div>
    <span @click="updateMenuList">
      <img :src=menu.image alt="menu.img" width="50" height="50">
      {{ menu.title }}
      {{ menu.price }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    updateMenuList() {
      this.$store.commit('updateMenuList', this.menu)
    }
  }
}
</script>

<style>

</style>