<template>
  <li @click="selectVideo">
    <img :src="youtubeImageSrc" alt="image">
    <span>{{ video.snippet.title }}</span>
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods: {
    selectVideo() {
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    youtubeImageSrc: function() {
      return this.video.snippet.thumbnails.default.url
    }
  }
}
</script>

<style>


</style>
