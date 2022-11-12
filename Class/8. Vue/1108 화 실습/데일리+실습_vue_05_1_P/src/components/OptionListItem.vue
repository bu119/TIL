<template>
  <div>
    <span>
      {{ option.type }}
      <button id="bnt" @click="decrease">-</button>
      {{ option.count }}
      <button id="bnt" @click="increase">+</button>
    </span>
  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$store.commit('increase', this.option)
    },
    decrease() {
      this.$store.commit('decrease', this.option)
    },
  }
}
</script>

<style>
#bnt {
  width:30px;
  height:30px;
  border-radius:75px;
  text-align:center;
  margin:5px;
  font-size:12px;
  vertical-align:middle;
}

</style>