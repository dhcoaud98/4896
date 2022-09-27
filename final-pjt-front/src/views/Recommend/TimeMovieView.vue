<template>
  <div>
    <div class='container'>

        <h2 class="text-center" style="color: #4C0070;">현재 시간과 어울리는 영화</h2>
        <p class="text-center" style="color: #4C0070;">지금 분위기에 어울리는 영화를 보고싶으신가요?</p>
        <br>
        <div v-for="(movie, idx) in timemovies" :key="idx">
          <div class="d-flex justify-content-center">
            <div class="card mb-2 border-3 border-gray" style="width: 800px; height: 420px; background-color: #FFEEEE;">
            <div class="row g-0" style="color: #4C0070;">
              <div class="col-md-4">
                <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="img-fluid m-2 rounded border border-5 border-dark"  alt="movie_img">
              </div>
              <div class="col-md-8 b-10">
                <div class="card-body m-20"> 
                  <h2 class="card-title fw-bold">{{ movie.title }}</h2>
                  <p class="card-text m-0" v-if="!movie.overview">줄거리가 제공되지 않습니다.</p>
                  <p class="card-text m-0" v-if="movie.overview">{{ movie.overview }}</p>
                  <p class="card-text m-0"> 상영시간 : {{ movie.runtime }}분</p>
                  <p class="card-text m-0"> 평점 : {{ movie.vote_average }}/10</p>
                  <p class="card-text m-0"> 인기도 : {{ movie.popularity }} </p>
                  <p class="card-text m-0">
                    <span v-for="genre in genres" :key="genre.pk">
                      <p v-if="genre.id === movie.genre[0]"> 장르 : {{ genre.name }}</p>
                    </span>
                  </p>
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
  name: 'TimeMovieView',
  computed: {
      ...mapGetters(['timemovies', 'genres'])
    },
  methods: {
      ...mapActions(['recommendMovies', 'getGenres',])
    },
  created() {
      this.recommendMovies()
      this.getGenres()
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