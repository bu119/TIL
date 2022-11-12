<template>
  <div id="app">
    <h1>Youtube Project</h1>
    <header>
      <TheSearchBar @input-change="OnInputChange"/>
    </header>
    <section>
      <VideoDetail :video="selectedVideo"/>
      <VideoList 
      :videos="videos"
      @select-video="onSelectVideo"
      />
      <!-- 비디오리스트를 하위폴더로 보냄 bind - 뒤에께 밑에 리스트 -->
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

const API_KEY = 'AIzaSyAS13y2LDZzVIhL_0CFgLfC8VWmmOdVoco'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data: function() {
    return {
      inputValue: null,
      videos: [],
      selectedVideo: null,
    }
  },

  methods: {
    OnInputChange(inputData) {
      // console.log(inputData)
      this.inputValue = inputData

      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue
      }

      axios({
        method: 'get',
        url: API_URL,
        params,
      })
      .then(res => {
        // console.log(res)
        this.videos = res.data.items
        console.log(this.videos)
      })
      .catch(err => {
        console.log(err)
      })
    },
    onSelectVideo(video){
      this.selectedVideo = video
      console.log(this.selectedVideo)
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 60px;
}
</style>
