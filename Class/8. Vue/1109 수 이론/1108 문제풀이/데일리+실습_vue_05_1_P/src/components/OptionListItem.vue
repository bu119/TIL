<template>
  <div>
    <li class="option-list-card flex justify-between items-center">
      <div>{{ option.type }}</div>
      <div class="flex items-center">
        <button @click="decrease">&#8722;</button>
        <div>{{ option.count }}</div>
        <button @click="increase">&#43;</button>
      </div>
    </li>
</div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$emit('increase', this.option)
    },
    decrease() {
      this.$emit('decrease', this.option)
    },
  },
}
</script>

<style>
.option-list-card {
  color: #3F3F46;
  border: 1px solid black;
  border-radius: 12px;
  padding: 12px 12px;
  margin: 14px 0;
  height: 74px;
}
.option-list-card button {
  width: 2rem;
  height: 2rem;
  padding: 7px;
  border-radius: 50%;
  margin: 12px 12px;
}
</style>