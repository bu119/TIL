<template>
  <div class='lotto'>
    <h1>로또</h1>
  </div>
</template>

<script>
export default {
  name: 'LottoView',
  data() {
    return {
      lottoNum: this.$route.params.userName
    }
  }

}
</script>

<style>

</style>