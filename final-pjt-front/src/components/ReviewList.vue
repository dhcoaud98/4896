<template>
  <div class="review-list">
    <ul>
      <review-list-item
        v-for="review in reviews"
        :review="review"
        :key="review.pk">
      </review-list-item>
    </ul>

    <review-list-form></review-list-form>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem'
import ReviewListForm from '@/components/ReviewListForm'

export default {
  name: 'ReviewList',
  components: { ReviewListItem, ReviewListForm },
  props: {reviews: Array},
}
</script>

<style scoped>

</style>
