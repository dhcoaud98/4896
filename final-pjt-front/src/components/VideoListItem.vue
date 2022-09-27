<template>
  <div @click="selectVideo">
    <img :src="youtubeImageSrc" alt="">
    {{ video.snippet.title | stringUnescaped }}
    <br>

  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VedioListItem',
  props:{
    video: Object,
  }, 
  computed:{
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  }, 
  // computed로 바꿔서 사용할 수도 있음
  filters: {
    stringUnescaped: function (rowText){
      return _.unescape(rowText)
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)  
    }
  }
}

</script>

<style>

</style>