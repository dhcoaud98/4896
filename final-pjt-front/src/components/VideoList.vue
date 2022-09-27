<template>
  <div>
    <div class="d-flex justify-content-center row">
      <video-list-item
        v-for="video in videos" 
        :key='video.id.vidoeId'
        :video='video'
        @select-video="selectVideo"
        >
      </video-list-item>
    </div>
  </div>
</template>


<script>
import VideoListItem from '@/components/VideoListItem'


export default {
  name: 'VedioList',
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  }, 
  methods: {
    selectVideo: function (video) {
      this.$emit('select-video', video)  
    }
  }
}

</script>

<style>

</style>