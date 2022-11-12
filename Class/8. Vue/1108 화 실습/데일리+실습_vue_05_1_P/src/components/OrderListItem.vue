<template>
  <div>
    <span>
      <img :src=order.menu.image alt="menu.img" width="50" height="50">
      {{ order.menu.title }}
      {{ order.size.name }}
    </span>
  </div>

</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    // totalPrice: function () {
    // },
  },
}
</script>

<style>
</style>