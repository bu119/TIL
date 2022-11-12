<template>
  <!-- 하나의 요소만 가능 -->
  <div>
    <h1>This is my component</h1>
    <MyChild 
      static-props="component에서 child로"
      :dynamic-props="dynamicProps"
      @click-to-parent="parentGentEvent"
      @child-input="getDynamicData"
    />
  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  components: {
    MyChild,
  },
  data: function() {
    return {
      dynamicProps: "It's in data!"
    }
  },
  methods: {
    parentGetEvent(inputData) {
      console.log('자식에서 발생한 이벤트')
      console.log(inputData)
    },
    getDynamicData: function(inputData){
      console.log(`child component로 부터 ${inputData}를 입력받음!`)
    }
  }
}
</script>

<style>

</style>