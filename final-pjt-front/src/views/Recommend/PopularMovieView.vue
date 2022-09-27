<template>
  <div>
    <div class='container'>

        <h2 class="text-center" style="color: #4C0070;">현재 인기 있는 영화</h2>
        <p class="text-center" style="color: #4C0070;">평점이 8점 이상인 인기많은 영화를 만나보세요!</p>
        <br>
        <div v-for="(movie, idx) in popularmovies" :key="idx">
          <div class="d-flex justify-content-center">
            <div class="card mb-2 border-3 border-gray" style="width: 800px; height: 420px; background-color: #FFEEEE;">
            <div class="row g-0" style="color: #4C0070;">
              <div class="col-md-4">
                <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="img-fluid m-2 rounded border border-5 border-dark"  alt="movie_img">
              </div>
              <div class="col-md-8">
                <div class="card-body m-20"> 
                  <h2 class="card-title fw-bold">{{ movie.title }}</h2>
                  <p class="card-text" v-if="!movie.overview">줄거리가 제공되지 않습니다.</p>
                  <p class="card-text" v-if="movie.overview">{{ movie.overview }}</p>
                  <p> 상영시간 : {{ movie.runtime }}분</p>
                  <h4 class="card-text"> 평점 : {{ movie.vote_average }}/10</h4>
                  <p class="card-text"> 인기도 : {{ movie.popularity }} </p>
                  <router-link 
                    :to="{ name: 'movie', params: {moviePk: movie.pk } }" 
                    style="color: #E9A6A6;">🎦 영화 더보기</router-link>
                </div>
              </div>
            </div>
            </div>
          </div>
        </div>

    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'PopularMovieView',
  components: {
    },
  computed: {
      ...mapGetters(['popularmovies'])
    },
  methods: {
      ...mapActions(['recommendMovies'])
    },
  created() {
      this.recommendMovies()
    },

}
</script>

<style scoped>
.card-text {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3; /* 라인수 */
    -webkit-box-orient: vertical;
    word-wrap:break-word; 
    line-height: 1.2em;
    height: 3.6em;
}
</style>