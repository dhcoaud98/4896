<template>
  <div style="height: 720px;">
    <h1 class="text-center" style="color: #4C0070;">Signup</h1>
    <p class="text-center" style="color: #4C0070;">회원가입을 진행해주세요</p>
    <br>
    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div class="d-flex justify-content-center">
        <label class="p-2" style="color: #4C0070;" for="username">Username : </label>
        <input  v-model="credentials.username" type="text" id="username" required/>
      </div>
      <br>

      <div class="d-flex justify-content-center">
        <label class="p-2" style="color: #4C0070;" for="password1">Password : </label>
        <input v-model="credentials.password1" type="password" id="password1" required />
      </div>
      <br>

      <div class="d-flex justify-content-center">
        <label class="p-2" style="color: #4C0070;" for="password2">Password : </label>
        <input v-model="credentials.password2" type="password" id="password2" required />
      </div>
      <br>

      <div class="d-flex justify-content-center">
        <button style="color: #4C0070;">Signup</button>
      </div>

    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>
