<template>
  <div class="col" >
    <!-- 영화를 카드 형태로 가져옴 -->
    <div class="card m-2 background-color: #4C0070;" style="width: 21rem; background-color: #4C0070;">
      <img :src="movieImage" alt="poster_img" style="width:320px" class="m-2" >
      <div class="card-body">
        <h5 class="card-text text-center" style="color: #E9A6A6;">{{ movie.title }}</h5>
        <p class="card-text" style="color: #E9A6A6;">{{ movie.overview }}</p>
        <router-link 
          :to="{ name: 'movie', params: {moviePk: movie.pk } }" 
          style="color: #E9A6A6;">더보기</router-link>
      </div>
      <br>
    </div>
  </div>
</template>

<script>

export default {
    name:'MovieCard',
    props: {
        movie:{
            type: Object,
        }
    },
    computed:{
       movieImage: function () {
          return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
       },
    },
  }
</script>

<style scoped>

.card:hover img{
  transform: scale(1.2);
  box-shadow: 0 10px 10px #4C0070, 0 4px 8px #4C0070;
}

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