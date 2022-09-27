<template>
  <div class="container" style="height: 720px;">
    <h1 class="text-center" style="color: #4C0070;">Logout</h1>
    <br>
    <p class="text-center">로그아웃 되었습니다. 서비스를 이용하시려면 다시 <router-link :to="{ name: 'login' }" style="color: #E9A6A6;">로그인</router-link> 해주세요!</p>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    methods: {
      ...mapActions(['logout'])
    },
    computed: {
      ...mapGetters(['isLoggedIn'])
    },
    created() {
      if (this.isLoggedIn) {
        this.logout()
      } else {
        alert('잘못된 접근')
        this.$router.back()
      }
    },
  }
</script>

<style></style>
