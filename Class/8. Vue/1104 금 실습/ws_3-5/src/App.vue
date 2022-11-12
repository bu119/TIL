<template>
  <div id="app">
    <h2>App</h2>
    <p><input type="text" v-model="appData"></p>
    <!-- v-model은 양방향이라 이벤트를 줄 필요없음 -->
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <AppParent
      :app-data="appData"
      :parent-data="parentData"
      :child-data="childData"
      @child-input-change="onChildInputChange"
      @parent-input-change="onParentInputChange"
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'


export default {
  name: 'App',
  components: {
    AppParent,
  },
  data: function (){
    return {
      appData: null,
      parentData: null,
      childData: null,
    }
  },
  methods: {
    onChildInputChange(inputData){
      this.childData = inputData
    },
    onParentInputChange(inputData){
      this.parentData = inputData
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
