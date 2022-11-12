<template>
  <div id="app" class="container">
    <h1>Coffee Order App</h1>
    <div id="bigsize">
      <MenuList/>
      <SizeList/>
      <OptionList/>
    </div>
    <button id="basket" @click="addOrder">장바구니 담기</button>
    <div id="ordertext">
      <h3>주문 내역</h3>
      <OrderList/>
    </div>
  </div>
</template>
<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'
import OptionList from '@/components/OptionList'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OrderList,
    OptionList,
  },
  methods: {
    addOrder() {
      this.$store.commit('addOrder')
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}

#bigsize {
  background-color: rgb(233, 233, 233);
  display: flex;
  justify-content: space-evenly;
  padding: auto;
  margin: 10px;
}

h1 {
  text-align: center;
}

#ordertext {
  background-color: rgb(233, 233, 233);
  display: flex;
  justify-content: space-evenly;
  padding: auto;
  margin: 10px;

}

#basket {
  width: 100%;
  background-color: rgb(25, 201, 25);
  border: none;
  color: white;
  border-radius: 5px;
  padding: 10px 30px;
  margin: 10px;
}


</style>
