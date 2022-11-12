<template>
  <div>
    <h1>로또</h1>
    <button @click="getNumbers">Get Lucky Numbers</button>
    <p>{{ selectedNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data() {
    return{
      sampleNums: [],
      selectedNums: [],
    }
  },
  methods: {
    getNumbers(){
      this.sampleNums = _.range(1,46)
      this.selectedNums = _.sampleSize(this.sampleNums, this.$route.params.lottoNum)
      this.selectedNums = _.sortBy(this.selectedNums)
    }
  }
}
</script>

<style>

</style>