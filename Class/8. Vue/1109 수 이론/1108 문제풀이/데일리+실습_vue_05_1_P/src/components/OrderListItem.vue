<template>
  <li class="order-overview-card flex justify-between">
    <div class="flex">
      <img :src="order.menu.image" alt="">
      <div>
        <p>{{ order.menu.title }}</p>
        <p>사이즈: {{ order.size.name }}</p>
      </div>
    </div>
    <div>
        <p>가격: {{ totalPrice }}원</p>
        <span v-for="option in order.option" :key="option.type">
        {{ option.type }} {{ option.count }}회 |
      </span>
    </div>
  </li>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    totalPrice: function () {
      const menu = this.order.menu.price
      const size = this.order.size.price
      const option = this.order.option.reduce((acc, op) => acc + op.price * op.count , 0)
      return menu + size + option
    },
  },
}
</script>

<style>
  .order-overview-card{
    color : #3f3f46;
    border-bottom: 1px solid #D1D5DB;
    padding: 20px 0px;
    margin: 14px 0;
  }
  .order-overview-card img{
    width: 50px;
    height: 50px;
    object-fit: cover;
    border-radius: 12px;
    margin-right: 12px;
  }
</style>