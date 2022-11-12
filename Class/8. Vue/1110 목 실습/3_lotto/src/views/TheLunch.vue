<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="pickLunch" >Pick Lunch</button>
    <p>{{ selectedLunch }}</p>
    <br>
    <h2>로또를 뽑아보자</h2>
    <button @click="PickLotto">Pick Lotto</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data() {
    return {
      lunch : ['전복굴국밥', '소고기장칼국수'],
      selectedLunch: null,
    } 
  },
  methods: {
    pickLunch(){
      this.selectedLunch = _.sample(this.lunch)
    },
    PickLotto(){
      this.$router.push({name: 'lotto', params: { lottoNum: 6 }})
    }
  },
}
</script>

<style>

</style>