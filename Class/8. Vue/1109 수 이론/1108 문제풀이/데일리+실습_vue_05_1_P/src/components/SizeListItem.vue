<template>
  <div
    class="size-list-card flex justify-between items-center"
    :class="{'selected': size.selected}"
  >
    <div>{{ size.name }}</div>
    <div>{{ size.price }}</div>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
}
</script>

<style>
.size-list-card {
color: #3F3F46;
border: 1px solid black;
border-radius: 12px;
padding: 20px;
margin: 14px 0;
height: 74px;
}
.size-list-card:hover {
cursor: pointer;
}
.selected {
color: white;
background: #059669;
}
</style>