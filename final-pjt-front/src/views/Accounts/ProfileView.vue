<template>
  <div>
    <h1 class="text-center fw-bold">{{ profile.username }}님의 프로필</h1>
    <hr>
    <div class="row row-cols-1 row-cols-md-3 d-flex justify-content-center">
      <div class="col card" style="width: 18rem;">
        <h2 class="col">📰 create article</h2>
        <ul class="list-group list-group-flush">
          <li v-for="article in profile.articles" :key="article.pk" class="list-group-item">
            <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.pk }} . {{ article.title }}
            </router-link>
          </li>
        </ul>
      </div>

      <div class="col card" style="width: 18rem;">
       <h2 class="col">❤️ like article</h2>
        <ul class="list-group list-group-flush">
          <li v-for="article in profile.like_articles" :key="article.pk" class="list-group-item">
            <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.pk }} . {{ article.title }}
            </router-link>
          </li>
        </ul>
      </div>

      <!-- <div class="col card" style="width: 18rem;">
        <h2 class="col">🧾 작성한 리뷰</h2> -->
          <!-- <ul class="list-group list-group-flush" v-for="review in reviews" :key="review.pk" >
            <li v-if="review">
                <router-link 
                  :to="{ name: 'movie', params: { moviePk: movie.pk } }" 
                  style="color: #E9A6A6;">{{ review.pk }} {{ }} </router-link>
            </li>
          </ul> -->
      <!-- </div> -->
    </div>
    <hr>

    <div>
      <h2 class="text-center">📽️ watch list movie</h2>
        <h4 class="text-center">내가 찜한 영화를 한번에 확인하세요!</h4>
        <br>
          <div class="row row-cols-1 row-cols-md-4 ms-5 ">
            <!-- 그리드 카드 형태로  -->
            <like-movie-card v-for="movie in profile.like_movies" :key="movie.pk" :movie="movie"> 
            </like-movie-card>      
          </div>
    </div>
    
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import LikeMovieCard from '@/components/LikeMovieCard'

export default {
  name: 'ProfileView',
  components:{
    LikeMovieCard
  },
  computed: {
    ...mapGetters(['profile',]),
    movieImage: function () {
      return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
    },
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
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