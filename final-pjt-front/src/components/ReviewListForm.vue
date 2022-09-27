<template>
  <form @submit.prevent="onSubmit" class="review-list-form">
    <label for="review" class="p-2">review : </label>
    <input type="text" id="review" v-model="content" required>
    <button class="btn btn-dark mx-1">작성하기</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ moviePk: this.movie.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>

</style>