<template>
  <div>
    <h2>AppParent</h2>
    <input type="text" @change="onParentInputChange">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <!-- 데이터 다 내리기 -->
    <AppChild
      :app-data="appData"
      :parent-data="parentData"
      :child-data="childData"
      @child-input-change="onChildInputChange"
    />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  components: {
    AppChild,
  },
  props: {
    appData: String,
    parentData: String,
    childData: String,
  },
  methods: {
    onChildInputChange(inputData){
      // console.log(inputData)
      this.$emit('child-input-change', inputData)
    },
    onParentInputChange(event){
      //console.log(event)
      this.$emit('parent-input-change', event.target.value)
    }
  }
}
</script>

<style>

</style>