<template>
  <div id="app" style="background-color: #EEEEEE;">
    <nav-bar></nav-bar>
    <!-- <hr /> -->
    <br>
    <router-view></router-view>
  </div>
</template>


<script>
  import NavBar from '@/components/NavBar.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar },
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>

<style></style>
