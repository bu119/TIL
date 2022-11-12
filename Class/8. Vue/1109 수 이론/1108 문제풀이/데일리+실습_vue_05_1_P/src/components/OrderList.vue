<template>
  <div>
    <div>
      <h1>주문내역</h1>  
      <p>총 {{ totalOrderCount }}건: {{ totalOrderPrice }}원</p>
    </div>
    <ul>
      <OrderListItem
        v-for="order in orderList"
        :key="order.title"
        :order="order"
      />
    </ul>
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'
export default {
  name: 'OrderList',
  components: {
    OrderListItem
  },
  computed: {
    orderList: function () {
      return this.$store.state.orderList
    },
    totalOrderCount: function () {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice: function () {
      return this.$store.getters.totalOrderPrice
    },
  },
}
</script>

<style>
</style>