<template>
  <div>
    <h1 class="text-center">게시판</h1>
    <router-link style=text-decoration:none;
      :to="{ name: 'articleNew' }" >
      <div class="d-flex justify-content-center">
        <a>새로운글 작성하기</a> 
      </div>
    </router-link>
    
    <hr>
    <div class="d-flex justify-content-right">
      <ul>
        <span v-for="article in articles" :key="article.pk" class="fw-bold">
          작성자 : 
          <!-- 작성자 -->
          {{ article.user.username }}
          <br>
          <!-- 글 이동 링크 (제목) -->
          title : 
          <router-link style=text-decoration:none;
            :to="{ name: 'article', params: {articlePk: article.pk} }">
            {{ article.title }}
          </router-link>

          <!-- 댓글 개수/좋아요 개수 -->
          <br>
          <p>댓글 : {{ article.comment_count }}개 | 좋아요 : {{ article.like_count }}개</p> 
          <hr>
        </span>
      </ul>
    </div>

   
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles'])
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style>
</style>
