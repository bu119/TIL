<template>
<!-- 최상위 태그가 존재해야한다. -->
  <div class="border"> 
    <h1>이거는 내가 만든 새로운 컴포넌트다!</h1>
    <MyComponentItem/>
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'
export default {
  name: 'MyComponent',
  // 2. 등록하기
  MyComponentItem,
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>