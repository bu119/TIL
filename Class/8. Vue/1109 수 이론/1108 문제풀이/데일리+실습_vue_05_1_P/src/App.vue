<template>
  <div id="app">
    <h1 class="flex justify-center">Coffee Order App</h1>
    <div class="order-board flex justify-between">
      <MenuList/>
      <SizeList/>
      <OptionList />
    </div>
    <div class="order-confirm flex justify-center">
      <button @click="addOrder">장바구니 담기</button>
    </div>
    <div>
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
  methods:{
    addOrder(){
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

/* container */
#app{
  margin: auto;
  max-width: 1280px;
}
#app h1 {
  margin: 24px 0;
}
/* global utils */
.flex {
display: flex;
}
.flex-column {
flex-direction: column;
}
.justify-center {
justify-content: center;
}
.justify-between {
justify-content: space-between;
}
.items-center {
align-items: center;
}
/* order */
.order-board {
  background: #F3F4F6;
  padding: 24px;
  border-radius: 12px;
  gap: 1rem;
}

.order-board > div {
  background: white;
  flex: 1;
  padding: 24px;
  border-radius: 12px;
}

.order-confirm {
  margin: 24px 0;
}

.order-confirm button { 
  font-size: 1.5rem;
  padding: 12px;
  width: 100%;
  border: none;
  border-radius: 12px;
  background: #059669;
  color: white;
}

.order-confirm button:hover {
  cursor: pointer;
  opacity: 0.8;
  transition: 0.2s;
}
</style>
