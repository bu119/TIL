<template>
  <div>
    <h1>3. 옵션을 고르세요.</h1>
    <ul class="option-list">
      <OptionListItem
        v-for="option in optionList"
        :key="option.name"
        :option="option"
        @increase="increase(option)"
        @decrease="decrease(option)"
      />
    </ul>
  </div>
</template>

<script>
import OptionListItem from '@/components/OptionListItem'
export default {
  name: 'OptionList',
  components: {
    OptionListItem
  },
  computed: {
    optionList: function () {
      return this.$store.state.optionList
    },
  },
  methods: {
    increase: function (option) {
      const newOption={
        type: option.type,
        price: option.price,
        count: option.count + 1,
      }
        // console.log(option)
      this.$store.commit('updateOptionList', newOption)
    },
    decrease: function (option) {
      let count = option.count - 1

      if(count < 0){
        count = 0
      }
      const newOption = {
        type: option.type,
        price: option.price,
        count: count,
      }
      this.$store.commit('updateOptionList', newOption)
    },
  },
}
</script>

<style>
</style>