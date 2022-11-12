<template>
  <div id="app">
    <SideBar />
    <router-view/>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'
export default {
  name: 'App',
  components: {
    SideBar
  }
}

</script>

<style>
#app {
  color: #2c3e50;
  height: 100vh;
  display: grid;
  grid-template-columns: 1fr 4fr;
  -moz-column-gap: 1rem;
  column-gap: 1rem;
  padding: 3rem;
}

#main {
  border-radius: 0.5rem;
  border: 2px solid #2c3e50;
  display: flex;
  flex-direction: column;
  padding: 2rem;
}

</style>
