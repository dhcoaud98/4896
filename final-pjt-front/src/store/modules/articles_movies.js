import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'


import _ from 'lodash'
// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    articles: [],
    article: {},

    movies: [],
    movie: {},
    popularmovies: [],
    shortmovies: [],
    longmovies: [],
    adultmovies: [],
    timemovies: [],

    genres: [],
  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    popularmovies: state => state.popularmovies,
    shortmovies: state => state.shortmovies,
    longmovies: state => state.longmovies,
    adultmovies: state => state.aultmovies,
    timemovies: state => state.timemovies,

    genres: state => state.genres,


    articles: state => state.articles,
    article: state => state.article,
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username
    },
    isArticle: state => !_.isEmpty(state.article),
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.reviews = reviews),
    SET_POPULAR_MOVIES: (state, movies) => state.popularmovies = movies,
    SET_SHORT_MOVIES: (state, movies) => state.shortmovies = movies,
    SET_LONG_MOVIES: (state, movies) => state.longmovies = movies,
    SET_NOW_MOVIES: (state, movies) => state.timemovies = movies,
    // SET_VIDEOS: (state, videos) => state.videos = videos,

    SET_GENRES: (state, genres) => state.genres = genres,

    SET_ARTICLES: (state, articles) => state.articles = articles,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS: (state, comments) => (state.article.comments = comments),
  },
  
  actions: {
    fetchArticles({ commit, getters }) {
      /* 게시글 목록 받아오기
      GET: articles URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.articles.articles(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_ARTICLES', res.data)
        })
        .catch(err => console.error(err.response))
    },

    fetchArticle({ commit, getters }, articlePk) {
      /* 단일 게시글 받아오기
      GET: article URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */
      axios({
        url: drf.articles.article(articlePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_ARTICLE', res.data)
        })
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    getMovies({ commit, getters }) {
      /* 영화 목록 받아오기
      GET: movies URL (token)
        성공하면
          응답으로 받은 게시글들을 state.movies에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
            console.log(res.data)
            commit('SET_MOVIES', res.data)
        })
        .catch(err => console.error(err.response))
    },
    getMovie({ commit, getters }, moviePk) {
      /* 단일 영화 받아오기
      GET: movie URL (token)
        성공하면
          응답으로 받은 게시글들을 state.movies에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
            console.log(res.data)
            commit('SET_MOVIE', res.data)
        })
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    getGenres({commit, getters}) {
      /*
      영화 장르 데이터 가져오기
      */
      axios({
        url:drf.movies.genres(),
        method:'get',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_GENRES', res.data)
        })
        .catch(err => console.error(err.response))

    },

    recommendMovies({ commit, getters }) {
      /* 추천영화 목록 받아오기
        성공하면
          응답으로 받은 게시글들을 state.movies에 저장
        실패하면
          에러 메시지 표시
      */

      axios({
        url: drf.movies.recommend(),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => {
            console.log(res.data)
            commit('SET_SHORT_MOVIES', res.data[0])
            commit('SET_LONG_MOVIES', res.data[1])
            commit('SET_POPULAR_MOVIES', res.data[2])
            commit('SET_NOW_MOVIES', res.data[3])
          })
        .catch(err => console.error(err.response))
    },

    createArticle({ commit, getters }, article) {
      /* 게시글 생성
      POST: articles URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      
      axios({
        url: drf.articles.articles(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
    },

    updateArticle({ commit, getters }, { pk, title, content}) {
      /* 게시글 수정
      PUT: article URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.articles.article(pk),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
    },

    deleteArticle({ commit, getters }, articlePk) {
      /* 게시글 삭제
      사용자가 확인을 받고
        DELETE: article URL (token)
          성공하면
            state.article 비우기
            AritcleListView로 이동
          실패하면
            에러 메시지 표시
      */
      
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.article(articlePk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_ARTICLE', {})
            router.push({ name: 'articles' })
          })
          .catch(err => console.error(err.response))
      }
    },

    likeArticle({ commit, getters }, articlePk) {
      /* 게시글 좋아요
      POST: likeArticle URL(token)
        성공하면
          state.article 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.articles.likeArticle(articlePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ARTICLE', res.data))
        .catch(err => console.error(err.response))
    },

    likeMovie({ commit, getters }, moviePk) {
      /* 영화 좋아요
      POST: likeMovie URL(token)
        성공하면 
        state.movie 갱신
      실패하면
        에러 메시지 표시
      */
      axios({
        url: drf.movies.likeMovie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_MOVIE', res.data)
        })
        .catch(err => console.error(err.response))
    },

		createComment({ commit, getters }, { articlePk, content }) {
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content }

      axios({
        url: drf.articles.comments(articlePk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateComment({ commit, getters }, { articlePk, commentPk, content }) {
      /* 댓글 수정
      PUT: comment URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content }

      axios({
        url: drf.articles.comment(articlePk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteComment({ commit, getters }, { articlePk, commentPk }) {
      /* 댓글 삭제
      사용자가 확인을 받고
        DELETE: comment URL (token)
          성공하면
            응답으로 state.article의 comments 갱신
          실패하면
            에러 메시지 표시
      */
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.articles.comment(articlePk, commentPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_ARTICLE_COMMENTS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },

      createReview({ commit, getters }, { moviePk, content }) {
        /* 리뷰 생성
        POST: reviews URL(리뷰 입력 정보, token)
          성공하면
            응답으로 state.movie의 reviews 갱신
          실패하면
            에러 메시지 표시
        */
        const review = { content }
  
        axios({
          url: drf.movies.reviews(moviePk),
          method: 'post',
          data: review,
          headers: getters.authHeader,
        })
          .then(res => {
            console.log(res.data)
            commit('SET_MOVIE_REVIEWS', res.data)
          })
          .catch(err => console.error(err.response))
      },

      updateReview({ commit, getters }, { moviePk, reviewPk, content }) {
        /* 리뷰 수정
        PUT: review URL(댓글 입력 정보, token)
          성공하면
            응답으로 state.movie의 reviews 갱신
          실패하면
            에러 메시지 표시
        */
        const review = { content }
  
        axios({
          url: drf.movies.review(moviePk, reviewPk),
          method: 'put',
          data: review,
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_MOVIE_REVIEWS', res.data)
          })
          .catch(err => console.error(err.response))
      },
  
      deleteReview({ commit, getters }, { moviePk, reviewPk }) {
        /* 리뷰 삭제
        사용자가 확인을 받고
          DELETE: review URL (token)
            성공하면
              응답으로 state.movie의 reviews 갱신
            실패하면
              에러 메시지 표시
        */
          if (confirm('정말 삭제하시겠습니까?')) {
            axios({
              url: drf.movies.review(moviePk, reviewPk),
              method: 'delete',
              data: {},
              headers: getters.authHeader,
            })
              .then(res => {
                commit('SET_MOVIE_REVIEWS', res.data)
              })
              .catch(err => console.error(err.response))
          }
        },
  },
}
