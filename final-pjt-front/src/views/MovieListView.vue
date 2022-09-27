<template>
  <div>
    <h1 class="text-center" style="color: #4C0070;">오늘의 랜덤 영화</h1>
    <br>
    <h3 class="text-center" style="color: #E9A6A6;"> 모든 영화를 만나보세요 :) </h3>
    <br>

    <div class="row row-cols-1 row-cols-md-4 ms-5 ">
      <!-- 그리드 카드 형태로  -->
      <movie-card v-for="(movie,idx) in movies" :key="idx" :movie="movie"> 
      </movie-card>   
         
    </div>

  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import MovieCard from '@/components/MovieCard'
  
  export default {
    name: 'MovieListView',
    components: {
      MovieCard,
    //   MovieDetail,
    },
    computed: {
      ...mapGetters(['movies'])
    },
    methods: {
      ...mapActions(['getMovies'])
    },
    created() {
      this.getMovies()
    },
  }
</script>

<style>
</style>