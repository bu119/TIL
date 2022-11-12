<template>
  <div>
    <nav>
      <router-link :to="{ name: 'all' }">모든</router-link>
      <router-link :to="{ name: 'today' }">오늘</router-link>
      <router-link :to="{ name: 'important' }">중요</router-link>
    </nav>

  </div>
</template>

<script>
export default {

}
</script>

<style>
nav {
  padding: 30px;
}

nav a {
  color: #2c3e50;
  font-size: 2rem;
  text-decoration: none;
}


nav a.router-link-exact-active {
  color: #42b983;
}

nav {
  border-radius: 0.5rem;
  border: 2px solid #2c3e50;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  height: 100vh;
}


</style>