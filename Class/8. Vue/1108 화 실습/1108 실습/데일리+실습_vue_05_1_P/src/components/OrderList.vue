<template>
  <div>
    <OrderListItem
      v-for="(order, index) in orderList" :key="index"
        :order="order"
    />
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'

export default {
  name: 'OrderList',
  components: {
    OrderListItem,
  },
  computed: {
    orderList() {
      return this.$store.state.orderList
    },
    // totalOrderCount: function () {
    // },
    // totalOrderPrice: function () {
    // },
  },
}
</script>

<style>
</style>