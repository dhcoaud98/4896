<template>
  <div class="container" style="height: 720px;">
    <h1 class="text-center" style="color: #4C0070;">Login</h1>
    <p class="text-center" style="color: #4C0070;">로그인을 진행해주세요</p>
    <br>
    <account-error-list v-if="authError"></account-error-list>


    <form @submit.prevent="login(credentials)">
      <div class="d-flex justify-content-center">
        <label class="p-2" style="color: #4C0070;" for="username">username : </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>
      <br>

      <div class="d-flex justify-content-center">
        <label class="p-2" style="color: #4C0070;" for="password">password : </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div>
      <br>

      <div class="d-flex justify-content-center">
        <button style="color: #4C0070;">Login</button>
      </div>
      <br>

      <div class="d-flex justify-content-center">
        <p>아직 회원이 아니신가요? 그렇다면 <router-link :to="{ name: 'signup' }" style="color: #E9A6A6;">회원가입</router-link>을 진행해주세요!</p>
      </div>
    
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style></style>
