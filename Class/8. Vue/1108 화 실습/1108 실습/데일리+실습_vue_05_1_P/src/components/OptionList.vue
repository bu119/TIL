<template>
  <div>
    <h1>3. 옵션을 고르세요.</h1>
    <ul class="option-list">
    </ul>
    <OptionListItem
      v-for="(option, index) in optionList" :key="index"
        :option="option"
    />
  </div>
</template>

<script>
import OptionListItem from '@/components/OptionListItem'

export default {
  name: 'OptionList',
  components: {
    OptionListItem,
  },
  computed: {
    optionList() {
      return this.$store.state.optionList
    },

  },
  methods: {
    // increase() {
    // },
    // decrease() {
    // },
  },
}
</script>

<style>
</style>