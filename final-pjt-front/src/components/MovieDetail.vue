<template>
<div class="movie-detail">
  <!-- 영화를 카드 형태로 가져옴 -->
  <div class="d-flex justify-content-center row">
    <div class="card mb-0 border-3 border-gray" style="width: 1500px; height: 600px; background-color: #FFEEEE;">
      <div class="row g-0" style="color: #4C0070;">
        <div class="col-md-4 text-center ">
          <img :src="movieImage" class="img-fluid m-2 rounded border border-5 border-dark mt-10" style="height: 30rem; width: 22rem;" alt="movie_img">
        </div>
        <div class="col-md-8 b-10">
          <div class="card-body "> 
            <h2 class="card-title fw-bold">{{ movie.title }}</h2>
            <p>{{ movie.release_date }}</p>
            <br>
            <h4 class="card-text fw-semibold"> 줄거리 </h4>
            <p>  {{ movie.overview }}</p>
            <p class="card-text"> 상영시간 : {{ movie.runtime }}분</p>
            <p class="card-text"> 평점 : {{ movie.vote_average }}</p>
            <p class="card-text"> 인기도 : {{ movie.popularity }} </p>
            <p class="card-text">
              <span v-for="genre in genres" :key="genre.pk">
                <p v-if="genre.id === movie.genre[0]"> 장르 : {{ genre.name }}</p>
              </span>
            </p>
            <a class="btn" @click="likeMovie(moviePk)">{{ likeMovieCount }} ❤️ </a><p></p>
          </div>
        </div>
      </div>
    </div>

    <div class="d-flex justify-content-center row">
      <div div class="card border-3 border-gray fw-semibold mt-2" style="width: 1500px; height: 200px; background-color: #FFEEEE;"> <h2> 🎇 [예고편] </h2>
        <br>
        <!-- <video-detail :selected-video="selectedVideo"></video-detail> -->
        <!-- <video-list 
          :videos="videos"
          @select-video="selectVideo">
        </video-list>  -->
      </div>
    </div>
    
  </div>

  <br>
  <div class="row-1">
    <div class="row d-flex justify-content-center">
      <div class="card row-2 m-1" style="max-width: 700px; background-color: #FFEEEE; ">
        <h2 class="fw-semibold mt-2">🔎 [{{ movie.title }}과(와) 비슷한 장르의 영화]</h2>
        <br>
          <span v-for="m in movies" :key="m.pk">
            <div v-if="m.genre[0] === movie.genre[0] && m.title != movie.title"> 
              <div class="card mb-3 " style="max-width: 540px; background-color: #F8ECD1; max-width: 700px;">
                <div class="row g-0 ">
                  <div class="col-md-4">
                    <img :src="`https://image.tmdb.org/t/p/w500/${m.poster_path}`" class="img-fluid rounded-start p-2" alt="...">
                  </div>
                  <div class="col-md-8 ">
                    <div class="card-body">
                      <br>
                      <h5 class="card-title"> 🙆🏻‍♀️ {{ m.title }}</h5>
                      <br>
                      <p class="card-text-similar">{{ m.overview }}</p>
                      <p class="card-text"><small class="text-muted">개봉 : {{ m.release_date }}</small></p>
                      <!-- <router-link 
                        :to="{ name: 'movie', params: {moviePk: m.pk } }" 
                        style="color: #E9A6A6;">🎦 영화 더보기</router-link> -->
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </span>

        <br>
      </div>

      <div class="card row-2 m-1" style="max-width: 500px; background-color: #FFEEEE;"> 
        <h2 class="fw-semibold mb-0 mt-2">🎞️ [리뷰]</h2>
        <p class="fw-bold mb-0 mt-2">관람객 리뷰 {{ likeReviewCount }}건</p>
        <hr>
        <review-list :reviews="movie.reviews"></review-list>
      </div>
    </div>
  </div>
</div> 
</template>

<script>
  
  import { mapGetters, mapActions } from 'vuex'
  import ReviewList from '@/components/ReviewList'
  // import VideoList from '@/components/VideoList'
  // import VideoDetail from '@/components/VideoDetail'
  import axios from 'axios'

  const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'


  export default {
    components: { 
      ReviewList, 
      // VideoList,
      // VideoDetail
    },
    name:'MovieDetail',
    data: function() {
      return {
        moviePk: this.$route.params.moviePk,
        videos: [],
        selectedVideo: null,
      }
    },
    computed:{
      ...mapGetters(['movie', 'genres', 'movies', ]),
      movieImage: function () {
          return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
      },
      likeMovieCount() {
        return this.movie.like_users?.length
      },
      likeReviewCount() {
        return this.movie.reviews.length
      },
    },
    methods:{
      ...mapActions([
        'getMovie',
        'likeMovie',
        'getGenres',
        'getMovies',
        // 'getVideos',
      ]),
      selectVideo: function (video) {
        this.selectedVideo = video
      },
      getVideo() {
        const params = {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: `${this.movie.title}` + '예고편'
        }
        axios({
          method: 'get',
          url: API_URL,
          params: params, 
        })
          .then(res => {
            console.log(res)
            this.videos = res.data.items
          })
          .catch(err=> {
            console.log(err)
          })
      }
      

    },
    created() {
      this.getMovie(this.moviePk)
      this.getGenres()
      this.getMovies()
      this.getVideo()
    },
  }

</script>

<style scoped>
.card-text-similar {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 5; /* 라인수 */
    -webkit-box-orient: vertical;
    word-wrap:break-word; 
    line-height: 1.2em;
    height: 3.6em;
}

</style>