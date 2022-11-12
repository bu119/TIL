<template>
  <div
    class="menu-card flex justify-between items-center"
    :class="{'selected': menu.selected}"
  >
    <img :src="menu.image" alt="">
    <p>{{ menu.title }}</p>
    <p>{{ menu.price }}원</p>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
}
</script>

<style>
.menu-card {
  color: #3F3F46;
  border: 1px solid black;
  border-radius: 12px;
  padding: 12px 12px;
  margin: 14px 0;
  height: 74px;
}

.menu-card:hover {
  cursor: pointer;
}

.selected {
  color: white;
  background: #059669;
}

.menu-card img {
  width: 50px;
  height: 50px;
  object-fit: cover;
  border-radius: 12px;
}

.menu-card button {
  width: 2rem;
  height: 2rem;
  padding: 7px;
  margin: 12px 0;
  border-radius: 50%;  
}
</style>