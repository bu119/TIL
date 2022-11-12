<template>
  <ul>
    <VideoListItem
      v-for="(video, idx) in videos"
      :key="idx"
      :video="video"
      @select-video="onSelectVideo"
    />
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    onSelectVideo(video) {
      // console.log(video)
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>