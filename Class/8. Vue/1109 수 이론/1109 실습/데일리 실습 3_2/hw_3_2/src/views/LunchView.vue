<template>
  <div class="lunch">
    <h1>점심메뉴</h1>
    <h2>로또를 뽑아보자</h2>
    <!-- <router-link :to="{ name: 'lotto' }">lotto</router-link> -->
    <button @click="toHome">Pick Lotto</button>

  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'LunchView',
  methods : {
    toLotto() {
      this.$router.push({name: 'lotto'})
    }
  }
}
</script>
