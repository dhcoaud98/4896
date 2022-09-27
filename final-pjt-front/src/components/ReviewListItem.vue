<template>
  <li class="review-list-item">
    <router-link :to="{ name: 'profile', params: { username: review.user.username } }">
      {{ review.user.username }}
    </router-link>: 
    
    <span v-if="!isEditing" class="fs-4 mb-1">{{ payload.content }}</span>
    <br>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button type="button" class="btn btn-dark btn-sm" @click="onUpdate">Update</button> |
      <button type="button" class="btn btn-dark btn-sm" @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.username === review.user.username && !isEditing">
      <button type="button" class="btn btn-dark btn-sm" @click="switchIsEditing">Edit</button> |
      <button type="button" class="btn btn-dark btn-sm" @click="deleteReview(payload)">Delete</button>
    </span>
    <hr>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListItem',
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.pk,
        content: this.review.content,
        // rank: this.review.rank
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.comment-list-item {
  border: 1px solid green;

}
</style>